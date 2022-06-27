# 🚨 Don't change the code below 👇
from turtle import st


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
totalheight = 0
x = 0
for n in student_heights:
    totalheight += n
    x += 1
print(round(totalheight/x))



