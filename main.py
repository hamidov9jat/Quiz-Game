from question_model import Question
from data import question_data

question_bank = []
for q_and_a in question_data:
    question_bank.append(Question(q_and_a['text'], q_and_a['answer']))

