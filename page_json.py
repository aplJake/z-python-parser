import json
from enum import Enum
# from single_test_parse import TaskEnum, AnswerEnum


class PageJsonify:
    def __init__(self):
        self.json_data = []

    def add_task(self, question_type, answer_type, test_number, image, question: list,
                 answers_arr: list):
        temp_task = {}
        temp_task["id"] = test_number
        temp_task["question_id"] = question_type
        temp_task["answer_id"] = answer_type

        temp_task["question_image"] = image
        if question_type == 1:
            temp_task["question"] = [{"paragraph": question[0]}]
        elif question_type == 2 or question_type == 3:
            temp_task["question"] = [{"paragraph": i} for i in question]

        temp_task["answers"] = [{"answer": i} for i in answers_arr]

        self.json_data.append(temp_task)
