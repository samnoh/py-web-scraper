from bs4 import BeautifulSoup
from .request import Request


class Page:
    """ Page Definition """

    _page = ""

    def __init__(self, url):
        request_result = Request(url).get()
        self._page = BeautifulSoup(request_result, "html.parser")

    @staticmethod
    def create(url, runs, params=""):
        page = Page(url + str(params))
        for run in runs:
            for key, value in run.items():
                getattr(page, key)(*value)
        return page

    def get_page(self):
        return self._page

    def set_page(self, page):
        self._page = page

    def find(self, tag, attrs={}):
        self.set_page(self._page.find(tag, attrs))

    def find_all(self, tag):
        self.set_page(self._page.find_all(tag))

    def get_each_text(self):
        result = []
        for r in self._page:
            result.append(r.string)
        self.set_page(result)
