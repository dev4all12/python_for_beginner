# Assign Grade to Student
student_marks = {'Ram': 92,
                 'Sem': 80,
                 'Hello': 64,
                 'Jami': 72,
                 'Wela': 39}
grade = {}
for student in student_marks:
    marks = student_marks[student]
    if marks > 90:
        grade[student] = "A+"
    elif marks > 80:
        grade[student] = "B+"
    elif marks > 70:
        grade[student] = "B"
    elif marks > 60:
        grade[student] = "C+"
    elif marks < 40:
        grade[student] = "Fail"

student = input("Enter name of Student: ").title()
print(grade[student])
