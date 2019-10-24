from .job_scraper.indeed_scraper import IndeedScraper
from .job_scraper.stackoverflow_scraper import StackoverflowScraper
from .job_scraper.seek_scraper import SeekScraper


class Scraper:
    """ Scraper Definition """

    @staticmethod
    def run_job_scraper(target, keyword, option=None):
        getattr(eval(target.capitalize() + "Scraper"), "create")(keyword, option)
