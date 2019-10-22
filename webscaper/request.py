import requests


class Request:
    """ Request Definition """

    def __init__(self, url):
        self.url = url

    def get_data(self, option="text"):
        result = getattr(self._data, option)
        if result == "function":
            return result()
        return result

    def set_data(self, data):
        self._data = data

    def get(self, params="", option="text"):
        self.set_data(requests.get(self.url + str(params)))
        return self.get_data(option)

    def post(self, data={}, option="json"):
        self.set_data(requests.post(self.url, data=data))
        return self.get_data(option)
