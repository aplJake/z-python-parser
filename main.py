from subject_page_parse import SingleSubjectParse
from single_test_parse import PageParser
# constants
WEBSITE_URL = "https://zno.osvita.ua"
SINGLE_SUBJECT_URL = "https://zno.osvita.ua/ukrainian"

if __name__ == "__main__":
    # create single subject test-link array
    subjectParse = SingleSubjectParse(SINGLE_SUBJECT_URL, WEBSITE_URL)
    z_subject_tests = subjectParse.parse_soup().test_urls
    # print(z_subject_tests)

    # page parsing
    test_link = z_subject_tests[0]
    page_parser = PageParser(test_link)
    page_parser.parse_soup()