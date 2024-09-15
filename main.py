from question_model import NewQuestion
from game_data import question_data
from quiz_brain import QuizBrain

"""This sets up the question bank."""
question_bank = []
for i in question_data:
    ques = i["text"]
    answ = i["answer"]
    newq = NewQuestion(ques, answ)
    question_bank.append(newq)

quiz = QuizBrain(question_bank, 7)

while quiz.still_has_questions():
    quiz.check_answer(quiz.next_question())
