from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    new_question = Question(i['text'], i['answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
quiz.final_score()

# For new Questions in the quiz change the questions in 'data.py'
# Open Trivya database to generate the questions based on the catagory.