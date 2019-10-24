from .job_scraper import JobScraper
from .constants import SO, SO_JOBLIST_URL, SO_APPLY_URL


class StackoverflowScraper(JobScraper):
    """ StackoverflowScraper Definition"""

    def __init__(self, keyword):
        self.keyword = keyword
        job_runs = [{"find_all": ["div", {"class": "-job"}]}]
        offset_runs = [
            {"find": ["div", {"class", "pagination"}]},
            {"find_all": ["a"]},
            {"get_each_value": ["get_text"]},
        ]
        super().__init__(SO_JOBLIST_URL, job_runs, offset_runs, "&pg=")

    def _extract_job(self, html):
        title = html.find("div", {"class": "-title"}).find("h2").find("a")["title"]
        company, location = html.find("div", {"class": "-company"}).find_all(
            "span", recursive=False
        )
        job_id = html["data-jobid"]

        return {
            "title": title,
            "company": company.get_text(strip=True),
            "location": location.get_text(strip=True).strip("-").lstrip(),
            "link": f"{SO_APPLY_URL}{job_id}",
        }

    def __str__(self):
        return SO
