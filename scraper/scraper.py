from bs.page import Page
from .helpers import convert_str_into_int


class Scraper:
    """ Scraper Definition """

    jobs = []
    offset_list = []

    def __init__(self, url, runs=None, limit=1):
        self.url = url
        self.get_offset_list(runs, limit)

    @classmethod
    def create(cls):
        return cls().get_jobs()

    def get_page(self, runs, params=""):
        return Page.create(url=self.url, runs=runs, params=params)

    def get_offset_list(self, runs, limit):
        if not runs:
            self.offset_list.append(0)
            return

        last_page = max(convert_str_into_int(self.get_page(runs)))
        for page in range(last_page):
            self.offset_list.append(page * limit)

    def get_jobs(self):
        pass
