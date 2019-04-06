from abstract_parser import AbstractParser


class PageParser(AbstractParser):
    def __init__(self, page_url):
        self.tasks_array = []
        return super().__init__(page_url)

    def parse_soup(self):
        col_main = self.soup.find("div", {"class": "col-main"})
        wrapper = col_main.find(id="wrap")
        tests = wrapper.select(".task-card .q-test")

        # get question and tasks
        for test in tests:

            # get test question
            question_paragraph = test.select_one(".question p")
            # case when question tag is inside div --> p
            if question_paragraph:
                question_text = question_paragraph.getText()
                print(question_text)
            # case when question text is only in div tag
            else:
                question_paragraph = test.select_one(".question")
                question_text = question_paragraph.getText()
                print(question_text)

            # get test answers
            answers = []
            # get answer soup from span
            answers_div = test.select(".answers .answer")
            for answer in answers_div:
                answer_text = answer.getText()
                print(answer_text[1:])