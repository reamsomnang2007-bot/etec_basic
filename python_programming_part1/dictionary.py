students = [
    {
        "id": 1,
        "name": "Somnang",
        "age" : 18,
        "gender" : "Male"
    },
    {
        "id": 2,
        "name": "dara",
        "age" : 18,
        "gender" : "Female"
    },
    {
        "id": 3,
        "name": "menghour",
        "age" : 18,
        "gender" : "Male"
    }
]
# add student to the list
students.append({
    "id": 4,
    "name": "mengchorng",
    "age" : 21,
    "gender": "Female"
})
# update student information
for student in students:
    if student['id'] == 2:
        student['name'] = "davit"
        student['age'] = 18.
        student['gender'] = "Male"
def display():
    for student in students:
        print(f"---------[ Student ]---------")
        for key, value in student.items():
            print(f"{key}: {value}")
        print("------------------------------")

display()

delete_student = int(input("Enter the student ID to delete: "))
for student in students:
    if student['id'] == delete_student:
        students.remove(student)
        break
display()

