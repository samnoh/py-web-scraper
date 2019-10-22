from constants import LIMIT, INDEED_JOBLIST_URL, INDEED_APPLY_URL
from webscaper.page import Page
from helpers import convert_str_into_int


class IndeedScraper:
    """ IndeedScrapper Definition """

    jobs = []

    @classmethod
    def create(cls):
        return cls().get_indeed_jobs()

    def get_indeed_page(self, runs, params=""):
        return Page.create(url=INDEED_JOBLIST_URL, runs=runs, params=params)

    def get_offset_list(self):
        runs = [
            {"find": ["div", {"class": "pagination"}]},
            {"find_all": ["a"]},
            {"get_each_value": ["string"]},
        ]
        last_page = max(convert_str_into_int(self.get_indeed_page(runs)))

        offset_list = []
        for page in range(last_page):
            offset_list.append(page * LIMIT)

        return offset_list

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

    def get_indeed_jobs(self):
        runs = [{"find_all": ["div", {"class": "jobsearch-SerpJobCard"}]}]

        offsets = self.get_offset_list()
        for offset in offsets:
            print(f"Scraping page {offsets.index(offset) + 1}...")
            results = self.get_indeed_page(runs, f"&start={offset}")
            for result in results:
                try:
                    self.jobs.append(self._extract_job(result))
                except Exception:
                    pass

        return self.jobs
