class QuizBrain:
    def __init__(self, questions, num_of_questions):
        import random
        self.question_bank = questions
        self.quiz_length = num_of_questions
        self.questions_done = []
        self.score = 0
        self.current_question = random.choice(self.question_bank)

    def next_question(self):
        import random
        self.quiz_length -= 1

        while self.current_question in self.questions_done:
            self.current_question = random.choice(self.question_bank)

        answer = input(f"Q.{len(self.questions_done) + 1}: {self.current_question.question}(True/False)? ")
        self.questions_done.append(self.current_question)
        return answer

    def still_has_questions(self):
        if self.quiz_length != 0:
            return True
        else:
            return False

    def check_answer(self, answer):
        if answer == self.current_question.answer:
            self.score += 1
            print("You got it!")
            print(f"The correct answer was {self.current_question.answer}.")
            print(f"Current Score: {self.score}/{len(self.questions_done)}")
        else:
            print("Welp.")
            print(f"The correct answer was {self.current_question.answer}.")

            if self.still_has_questions():
                print(f"Current Score: {self.score}/{len(self.questions_done)}")
            else:
                print(f"Your final score was {self.score}/{len(self.questions_done)}.\n Thanks for playing!")
