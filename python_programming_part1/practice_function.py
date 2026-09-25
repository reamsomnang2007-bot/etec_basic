print("----------{ Input }----------")
name = input("Enter your name: ")
gender = input("Enter your gender: ")
age = int(input("Enter your age: "))
s1 = float(input("Enter Score 1: "))
s2 = float(input("Enter Score 2: "))
s3 = float(input("Enter Score 3: "))
print("-----------------------------")
total = s1 + s2 + s3
average = total / 3
def check_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
print("----------{ Output }----------")
print(f"Name: {name}")
print(f"Gender: {gender}")
print(f"Age: {age}")
print(f"Score 1: {s1}")
print(f"Score 2: {s2}")
print(f"Score 3: {s3}")
print(f"Total Score: {total}")
print(f"Average Score: {average:.2f}")
print(f"Grade: {check_grade(average)}")
print("-----------------------------")