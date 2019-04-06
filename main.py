import requests
from bs4 import BeautifulSoup

MAIN_URL = "https://zno.osvita.ua/ukrainian/"

r = requests.get(MAIN_URL)

def parse_soup():
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup)


def save_html(html, path):
    with open(path, "wb") as f:
        f.write(html)


if __name__ == "__main__":
    parse_soup()
