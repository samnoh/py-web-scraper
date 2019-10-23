from .scraper import Scraper
from .constants import SO_JOBLIST_URL, SO_APPLY_URL


class StackoverflowScraper(Scraper):
    """ StackoverflowScraper Definition"""

    def __init__(self):
        runs = [
            {"find": ["div", {"class", "pagination"}]},
            {"find_all": ["a"]},
            {"get_each_value": ["get_text"]},
        ]
        super().__init__(SO_JOBLIST_URL, runs)

    def _extract_job(self, html):
        title = html.find("div", {"class": "-title"}).find("h2").find("a")["title"]
        company, location = html.find("div", {"class": "-company"}).find_all(
            "span", recursive=False
        )
        job_id = html["data-jobid"]

        return {
            "link": f"{SO_APPLY_URL}{job_id}",
            "title": title,
            "company": company.get_text(strip=True),
            "location": location.get_text(strip=True).strip("-").lstrip(),
        }

    def get_jobs(self):
        runs = [{"find_all": ["div", {"class": "-job"}]}]

        offsets = self.offset_list
        for offset in offsets:
            print(f"Scraping page {offsets.index(offset) + 1}...")
            results = self.get_page(runs, f"&pg={offset + 1}")
            for result in results:
                try:
                    self.jobs.append(self._extract_job(result))
                except Exception:
                    print(Exception)
        return self.jobs
