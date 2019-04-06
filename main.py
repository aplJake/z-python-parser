import requests
from bs4 import BeautifulSoup

WEBSITE_URL = "https://zno.osvita.ua"
MAIN_URL = "https://zno.osvita.ua/ukrainian"
page_tests_urls = []


r = requests.get(MAIN_URL)

def parse_soup():
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup)

    test_blocks = soup.select(".col-main .tests-block")
    # print(test_blocks)

    # getting urls from a tag
    #  from ul-test blocks
    for row in test_blocks:
        link = row.select_one(".test-item a")["href"]
        complete_link = WEBSITE_URL + link
        page_tests_urls.append(complete_link)


def save_html(html, path):
    with open(path, "wb") as f:
        f.write(html)


if __name__ == "__main__":
    parse_soup()
