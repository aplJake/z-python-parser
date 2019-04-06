import requests
from bs4 import BeautifulSoup

from abstract_parser import AbstractParser


class SingleSubjectParse(AbstractParser):
    def __init__(self, page_url, website_link):
        self.test_urls = []
        self.website_link = website_link
        return super().__init__(page_url)

    def parse_soup(self):
        test_blocks = self.soup.select(".col-main .tests-block")

        # getting urls from a tag  from ul-test blocks
        for row in test_blocks:
            link = row.select_one(".test-item a")["href"]
            complete_link = self.website_link + link
            self.test_urls.append(complete_link)

        return self
