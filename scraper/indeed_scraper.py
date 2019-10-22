from .scraper import Scraper
from .constants import LIMIT, INDEED_JOBLIST_URL, INDEED_APPLY_URL


class IndeedScraper(Scraper):
    """ IndeedScrapper Definition """

    def __init__(self):
        runs = [
            {"find": ["div", {"class": "pagination"}]},
            {"find_all": ["a"]},
            {"get_each_value": ["string"]},
        ]
        super().__init__(INDEED_JOBLIST_URL, runs, LIMIT)

    def _extract_job(self, html):
        title = html.find("div", {"class": "title"}).find("a")["title"]

        company = html.find("span", {"class": "company"})
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = company_anchor.string
        else:
            company = company.string

        location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
        job_id = html["data-jk"]

        return {
            "link": f"{INDEED_APPLY_URL}{job_id}",
            "title": title,
            "company": company.strip(),
            "location": location,
        }

    def get_jobs(self):
        runs = [{"find_all": ["div", {"class": "jobsearch-SerpJobCard"}]}]

        offsets = self.offset_list
        for offset in offsets:
            print(f"Scraping page {offsets.index(offset) + 1}...")
            results = self.get_page(runs, f"&start={offset}")
            for result in results:
                try:
                    self.jobs.append(self._extract_job(result))
                except Exception:
                    pass

        return self.jobs
