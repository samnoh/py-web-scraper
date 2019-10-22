from .scraper import Scraper
from .constants import SO_JOBLIST_URL


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
        return html["data-jobid"]

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
                    pass

        return self.jobs
