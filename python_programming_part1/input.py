name = input("Enter your Name: ")
gender = input("Enter your Gender: ")
age = int(input("Enter your Age: "))
score1 = int(input("Enter score 1: "))
score2 = int(input("Enter score 2: "))
score3 = int(input("Enter score 3: "))

total = score1 + score2 + score3
average = total / 3
print("=====[ Information Student ]=====")
print(f"Name: {name}")
print(f"Gender: {gender}")
print(f"Age: {age}")
print(f"Score 1: {score1}")
print(f"Score 2: {score2}")
print(f"Score 3: {score3}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print("=================================")
