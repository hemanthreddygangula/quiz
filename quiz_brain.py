class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0
    
    def still_has_questions(self):
        return self.q_number<len(self.q_list)
    
    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number+=1
        answer = input(f"Q.{self.q_number}: {current_question.text} (True/False): ")
        self.check_answer(answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score+=1
            print("You got it Right")
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}")
        print(f"Your score is {self.score}/{self.q_number}\n")

    def final_score(self):
        print("You have completed the QUIZ.")
        print(f"Your Final score is {self.score}/{self.q_number}")
