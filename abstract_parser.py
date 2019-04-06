from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup

class AbstractParser:
    def __init__(self, page_url):
        self.page_url = page_url
        self.r = requests.get(page_url)
        self.soup = BeautifulSoup(self.r.content, 'html.parser')
        super().__init__()
    
    @abstractmethod
    def parse_soup():
        pass