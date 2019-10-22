from constants import INDEED_URL, LIMIT
from webscaper.page import Page
from helpers import list_convert_into_int


class IndeedScraper:
    """ IndeedScrapper Definition """

    offset_list = []

    def __init__(self):
        self.get_offset_list()

    def get_indeed_page(self, runs, params=""):
        return Page.create(url=INDEED_URL, runs=runs, params=params)

    def get_offset_list(self):
        runs = [
            {"find": ["div", {"class": "pagination"}]},
            {"find_all": ["a"]},
            {"get_each_value": ["string"]},
        ]
        last_page = max(list_convert_into_int(self.get_indeed_page(runs)))

        for page in range(last_page):
            self.offset_list.append(f"{page*LIMIT}")

    def get_indeed_jobs(self):
        jobs = []
        runs = [{"find_all": ["div", {"class": "jobsearch-SerpJobCard"}]}]

        # for offset in self.offset_list:
        results = self.get_indeed_page(runs, f"&start={0}")

        for result in results:
            try:
                title = result.find("div", {"class": "title"}).find("a")["title"]
                company = result.find("span", {"class": "company"})
                company_anchor = company.find("a")
                if company_anchor is not None:
                    company = company_anchor.string.strip()
                else:
                    company = company.string.strip()
                jobs.append(f"{title} - {company}")
                print(title, company)
            except Exception:
                pass

        return jobs
