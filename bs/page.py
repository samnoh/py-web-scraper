import inspect
from bs4 import BeautifulSoup
from .request import Request


class Page:
    """ Page Definition """

    def __init__(self, url):
        request_result = Request(url).get()
        self._page = BeautifulSoup(request_result, "html.parser")

    @classmethod
    def create(cls, url, runs, params=""):
        page = cls(url + str(params))
        for run in runs:
            key = next(iter(run))
            getattr(page, key)(*run[key])
        return page._page

    def find(self, tag, attrs={}):
        self._page = self._page.find(tag, attrs)

    def find_all(self, tag, attrs={}):
        self._page = self._page.find_all(tag, attrs)

    def get_each_value(self, option="string"):
        result = []
        for r in self._page:
            data = getattr(r, option)
            if inspect.ismethod(data):
                result.append(data())
            elif data is not None:
                result.append(data)
        self._page = result

    def get_each_attr(self, attr):
        result = []
        for r in self._page:
            result.append(r[attr])
        self._page = result

    def get_each_find(self, tag, attrs={}):
        result = []
        for r in self._page:
            data = r.find(tag, attrs)
            if data is not None:
                result.append(data)
        self._page = result
