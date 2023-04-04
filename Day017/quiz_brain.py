class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.num_asked = 0
        
    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, true):
        if answer == true or answer.lower() == true[0].lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Incorrect.")
        
        print(f"The answer is: {true}")
        self.num_asked += 1
        self.question_number += 1
        
        
    def next_question(self):
        
        question = self.question_list[self.question_number]
        answer = input(f"Q{self.question_number + 1}: {question.text} (True/False): ")
        self.check_answer(answer, question.answer)
       
            