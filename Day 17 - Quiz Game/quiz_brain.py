class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]

        self.question_number += 1

        answer = input(f"Q.{self.question_number}: {current_question.text} True or False: ").lower()

        if self.checking_answer(answer, current_question.answer):
            self.score += 1
            print(f"Nice you got {self.score}/{self.question_number} questions right\n")
        else:
            print(f"Nice try... your score is {self.score}/{self.question_number}\n")

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def checking_answer(self, user_answer, correct_answer):
        return user_answer == correct_answer.lower()
