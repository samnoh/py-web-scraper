import requests
from bs4 import BeautifulSoup


class Page:
    """ Page Definition """

    _bs_result = ""

    def __init__(self, URL):
        request_result = requests.get(URL)
        self._bs_result = BeautifulSoup(request_result.text, "html.parser")

    @staticmethod
    def build(URL, runs):
        page = Page(URL)
        for run in runs:
            for key, value in run.items():
                getattr(page, key)(*value)
        return page

    def get_result(self):
        return self._bs_result

    def set_result(self, result):
        self._bs_result = result

    def find(self, tag, attrs={}):
        self.set_result(self._bs_result.find(tag, attrs))

    def find_all(self, tag):
        self.set_result(self._bs_result.find_all(tag))

    def get_each_text(self, tag, attrs={}):
        result = []
        for r in self._bs_result:
            result.append(r.find(tag, attrs).text)
        self.set_result(result)
