from enum import Enum
from abstract_parser import AbstractParser
from page_json import PageJsonify


# class TaskEnum(Enum):
#     SIMPLE = 1
#     SHORT_TEXT = 2
#     LONG_TEXT = 3
#     IMAGE = 4


# class AnswerEnum(Enum):
#     # multiple choise if answers lenght > 4
#     SIMPLE = 1
#     MULTILINE = 2


class PageParser(AbstractParser):
    def __init__(self, page_url):
        self.tasks_array = []
        self.page_json = PageJsonify()
        return super().__init__(page_url)

    def parse_soup(self):
        col_main = self.soup.find("div", {"class": "col-main"})
        wrapper = col_main.find(id="wrap")
        task_card = wrapper.select(".task-card")

        # get question and tasks
        for card in task_card:
            question_type = None
            answer_type = None
            question_text = []
            answers = []

            test_number = card.select_one(".counter").getText()
            # task number fix --> (Task 2 from 35)
            test_number = test_number.replace("Завдання ", "")
            test_number = test_number.split(' ', 1)[0]

            test = card.select_one(".q-test")
            # get test question
            question_paragraph = test.select(".question p")
            print(test_number, len(question_paragraph))
            # case when question tag is inside div --> p
            if question_paragraph and len(question_paragraph) == 1:
                question_type = 1
                question_text.append(question_paragraph[0].getText())

            elif question_paragraph and len(question_paragraph) == 3:
                question_type = 2
                for paragraph in question_paragraph:
                    question_text.append(paragraph.getText())

            elif question_paragraph and len(question_paragraph) > 3:
                question_type = 3
                for paragraph in question_paragraph:
                    question_text.append(paragraph.getText())

            # case when question text is only in div tag
            else:
                question_type = 1
                question_paragraph = test.select_one(".question")
                question_text.append(question_paragraph.getText())
                print(question_text)

            # get answer soup from span
            answers_div = test.select(".answers .answer")
            for answer in answers_div:
                answer_text = answer.getText()
                answers.append(answer_text[1:])

            answer_type = 2 if len(
                answers) > 4 else 1

            # add data to json
            self.page_json.add_task(
                question_type=question_type,
                answer_type=answer_type,
                test_number=test_number,
                question=question_text,
                answers_arr=answers)

        return self

    def printJson(self):
        print("\n" * 10)
        print(self.page_json.json_data)