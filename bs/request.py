import inspect
import requests


class Request:
    """ Request Definition """

    def __init__(self, url):
        self._url = url

    def get_data(self, option="text"):
        result = getattr(self._data, option)
        if inspect.isfunction(result):
            return result()
        return result

    def get(self, params="", option="text"):
        self._data = requests.get(self._url + str(params))
        return self.get_data(option)

    def post(self, data={}, option="json"):
        self._data = requests.post(self._url, data=data)
        return self.get_data(option)
