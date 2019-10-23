from .job_scraper import JobScraper
from .constants import SEEK, SEEK_JOBLIST_URL, SEEK_APPLY_URL


class SeekScraper(JobScraper):
    """ SeekScraper Definition """

    def __init__(self):
        job_runs = [{"find_all": ["article"]}]
        offset_runs = [
            {"find": ["p", {"class": "_1eeNbu7"}]},
            {"get_each_value": ["string"]},
        ]
        super().__init__(
            SEEK_JOBLIST_URL, job_runs, offset_runs, offset_params="?page="
        )
        # self.offset_list = [1, 2, 3, 4, 5, 6, 7]

    def _extract_job(self, html):
        title = html["aria-label"]
        company = html.find("a", {"data-automation": "jobCompany"}).get_text()
        location = html.find("strong").find("a").get_text()
        job_id = html["data-job-id"]

        return {
            "title": title,
            "company": company,
            "location": location,
            "link": f"{SEEK_APPLY_URL}{job_id}",
        }

    def __str__(self):
        return SEEK
