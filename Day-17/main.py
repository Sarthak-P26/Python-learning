from question_model import Question
from data import question_data

# questions = Question()

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]