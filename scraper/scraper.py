from .indeed_scraper import IndeedScraper
from .stackoverflow_scraper import StackoverflowScraper
from .constants import INDEED, SO


class Scraper:
    """ Scraper Definition """

    @staticmethod
    def run_job_scraper(target, option=None):
        if target == INDEED:
            IndeedScraper.create(option)
        elif target == SO:
            StackoverflowScraper.create(option)
