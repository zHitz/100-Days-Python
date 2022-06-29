class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list 
     
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False    
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer=input(f"{self.question_number} : {current_question.text} (True/False) ?: ")     
        self.check_answer(user_answer,current_question.answer)
        
    def check_answer(self,user_answer,correct_answer):
        if user_answer == correct_answer:
            self.score +=1
            print(f"You got it right!") 
            print(f"Your current score is: {self.score}") 
        else:
            print(f"You got it wrong!") 
            print(f"Your final score is: {self.score}/{len(self.question_list)}") 
            return False
        print(f"The correct answer was: {correct_answer}")