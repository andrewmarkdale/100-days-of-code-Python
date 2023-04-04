"""

Andrew Dale

Subject/Class:
100 Days of Code: The Complete Python Pro Bootcamp for 2023 by Dr. Angela Yu

Day:
17

Project:
Quiz game OOP

"""

from question_model import Question
from data import question_data


question_list = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    question_list.append(Question(text, answer))

