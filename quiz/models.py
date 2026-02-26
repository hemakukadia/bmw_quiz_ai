from datetime import datetime


class Question:

    def __init__(self, prompt, options, correct_index):
        self.prompt = prompt
        self.options = options
        self.correct_index = correct_index

    def is_correct(self, choice_index):
        return choice_index == self.correct_index


class QuizAttempt:


    def __init__(self, name, score, total):
        self.name = name
        self.score = score
        self.total = total
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")