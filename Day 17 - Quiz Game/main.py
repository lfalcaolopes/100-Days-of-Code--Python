from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    question_bank.append(Question(questions['text'], questions['answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
