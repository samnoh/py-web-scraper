from bs.page import Page
from helpers import convert_str_into_int
from output.output import Output

CONSOLE = "console"
CSV = "csv"


class JobScraper:
    """ JobScraper Definition """

    jobs = []
    offset_list = []

    def __init__(self, url, job_runs, offset_runs=None, offset_params="", limit=1):
        self.url = url
        self.job_runs = job_runs
        self.offset_params = offset_params
        self.get_offset_list(offset_runs, limit)

    @classmethod
    def create(cls, option=None):
        my_class = cls()
        jobs = my_class.get_jobs()
        if option == CONSOLE:
            Output.console_output(jobs)
        elif option == CSV:
            Output.csv_output(my_class, jobs, ["Title", "Company", "Location", "Link"])
        else:
            return jobs

    def get_page(self, runs, params=""):
        return Page.create(url=self.url, runs=runs, params=params)

    def get_offset_list(self, offset_runs, limit):
        if not offset_runs:
            self.offset_list.append(0)
            return
        last_page = max(convert_str_into_int(self.get_page(offset_runs)))
        for page in range(last_page):
            self.offset_list.append(page * limit)

    def get_jobs(self):
        offsets = self.offset_list
        for offset in offsets:
            print(f"Scraping {self} page {offsets.index(offset) + 1}...")
            results = self.get_page(self.job_runs, f"{self.offset_params}{offset}")

            for result in results:
                try:
                    self.jobs.append(self._extract_job(result))
                except Exception:
                    pass

        return self.jobs
