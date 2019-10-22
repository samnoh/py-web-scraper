from constants import INDEED_URL
from webscaper.Page import Page

runs = [
    {"find": ["div", {"class": "pagination"}]},
    {"find_all": ["a"]},
    {"get_each_text": ["span"]},
]
page = Page.build(INDEED_URL, runs)

print(page.get_result()[:-1])
