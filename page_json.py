import json

class PageJsonify:
    def __init__(self):
        self.json_data = []
    
    def add_task(self, question: str, answers_arr: list):
        temp_task = {}
        temp_task["question"] = question
        temp_task["answers"] = [{"answer": i} for i in answers_arr]

        self.json_data.append(temp_task)

