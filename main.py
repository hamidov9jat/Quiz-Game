from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q_and_a in question_data:
    question_bank.append(Question(q_and_a['question'], q_and_a['correct_answer'].lower()))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    is_exit = input("Do you want to exit 'y' or 'smth else to continue'? ").lower()
    if is_exit == 'y':
        break
print('Goodbye!')
