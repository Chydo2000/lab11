students = []
while 1:
    student_name = input("Enter student name:")

    if student_name == "":
        break
    else:
        students.append(student_name)

print("Student count:", len(students))
i = 0
while i < len(students):
    if i == len(students) - 1:
        print(students[i])
    else:
        print(students[i], end = ", ")
    
    i += 1