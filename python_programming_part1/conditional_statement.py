print("==========[ Input ]==========")
name = input("Enter your Name: ")
gender = input("Enter your Gender: ")
age = int(input("Enter your Age: "))
score1 = int(input("Enter score 1: "))
score2 = int(input("Enter score 2: "))
score3 = int(input("Enter score 3: "))
print("=============================")

total = score1 + score2 + score3
average = total / 3
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
elif average >= 50:
    grade = "E"
else:
    grade = "F"
print("=====[ Information Student ]=====")
print(f"Name: {name}")
print(f"Gender: {gender}")
print(f"Age: {age}")
print(f"Score 1: {score1}")
print(f"Score 2: {score2}")
print(f"Score 3: {score3}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
print("=================================")