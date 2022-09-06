class QuizBrain:
    def __init__(self, questions_list: list):
        self.score = 0
        self.question_number = 0
        self.questions_list = questions_list
        self.number_of_questions = len(questions_list)

    def still_has_questions(self):
        """Returns True if there are still questions left"""
        return self.question_number < self.number_of_questions

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.question_text} (True/False): ").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer: str, correct_answer: str):
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}.")

        print(f"\nYour current score is: {self.score}/{self.question_number}")
        print('\n')
