student = []
subjects = []
for i in range(3):
    name = str(input("enter name : "))
    student.append(name)
print(student)

for i in range(3):
    sub = str(input("enter subjects : "))
    subjects.append(sub)
print(subjects)

dict = {student[i] : subjects[i] for i in range(len(student))}
print(dict)
