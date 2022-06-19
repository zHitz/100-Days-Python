from turtle import st


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for n in student_scores:
    if student_scores[n] > 90 and student_scores[n] <= 100:
        student_grades[n] = 'Grade = "Outstading"'
    elif student_scores[n] > 80 :
        student_grades[n] = 'Grade = "Exceeds Expectations"'
    elif student_scores[n] > 70 :
        student_grades[n] = 'Grade = "Acceptable"'
    elif student_scores[n] <= 70:
        student_grades[n] = 'Grade = "Fail"'
    

# 🚨 Don't change the code below 👇
print(student_grades)





