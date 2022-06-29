
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for n in question_data:
    data = Question(n["text"],n["answer"])
    question_bank.append(data)
# print(question_bank[0].text)



quiz =QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print(f"Your final score is: {quiz.score}/{len(quiz.question_list)}")
# print(
    # len(quiz))
        