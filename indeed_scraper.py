from constants import INDEED_URL, LIMIT
from webscaper.page import Page
from helpers import list_convert_into_int


def get_indeed_pages(offset=0):
    indeed_page = Page.create(
        url=INDEED_URL,
        params=f"&start={offset}",
        runs=[
            {"find": ["div", {"class": "pagination"}]},
            {"find_all": ["a"]},
            {"get_each_text": []},
        ],
    )

    return max(list_convert_into_int(indeed_page.get_page()))


def extract_indeed_jobs(last_page):
    for page in range(last_page):
        print(f"{page*LIMIT}")
