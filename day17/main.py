import os
# Set work directory
os.chdir(r'C:\Users\p901kvb\Desktop\Python\100days\day17')

from quiz_brain import QuizBrain

# Import data
from data import question_data

class Question:
    def __init__(self, text, answer) -> None:
        self.text = text
        self.answer = answer


question_bank = [Question(q['text'], q['answer']) for q in question_data]
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")



