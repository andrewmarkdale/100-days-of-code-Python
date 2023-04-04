"""

Andrew Dale

Subject/Class:
100 Days of Code: The Complete Python Pro Bootcamp for 2023 by Dr. Angela Yu

Day:
17

Project:
Quiz game OOP using open quiz db (some of the formatting is off)

"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_list = []

for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    question_list.append(Question(text, answer))


quiz = QuizBrain(question_list)
quiz.next_question()

game_active = True
while quiz.still_has_questions(): 
    print(f"Total score: {quiz.score} out of {quiz.num_asked}.\n")
    quiz.next_question()

print(f"Final score: {quiz.score} out of {quiz.num_asked}.")
print("Out of questions, thank you for playing!")
