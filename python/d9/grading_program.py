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
    if student_scores[n] >= 91 and student_scores[n] <= 100:
        student_grades[n] = "Outstanding"
    elif student_scores[n] >= 81:
        student_grades[n] = "Exceeds Expectations"
    elif student_scores[n] >= 71:
        student_grades[n] = "Acceptable"
    else: 
        student_grades[n] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)