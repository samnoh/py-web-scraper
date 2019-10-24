from .job_scraper import JobScraper
from .constants import LIMIT, INDEED, INDEED_JOBLIST_URL, INDEED_APPLY_URL


class IndeedScraper(JobScraper):
    """ IndeedScrapper Definition """

    def __init__(self, keyword):
        self.keyword = keyword
        job_runs = [{"find_all": ["div", {"class": "jobsearch-SerpJobCard"}]}]
        offset_runs = [
            {"find": ["div", {"class": "pagination"}]},
            {"find_all": ["a"]},
            {"get_each_value": ["string"]},
        ]
        super().__init__(INDEED_JOBLIST_URL, job_runs, offset_runs, "&start=", LIMIT)

    def _extract_job(self, html):
        title = html.find("div", {"class": "title"}).find("a")["title"]
        company = html.find("span", {"class": "company"})
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = company_anchor.get_text(strip=True)
        else:
            company = company.get_text(strip=True)
        location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
        job_id = html["data-jk"]

        return {
            "title": title,
            "company": company,
            "location": location,
            "link": f"{INDEED_APPLY_URL}{job_id}",
        }

    def __str__(self):
        return INDEED
