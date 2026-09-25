import random
lowest_num = 1
highest_num = 100
number_guesses = 0
print("----------[ Welcome to Game Number guessing ]----------")
answer = random.randint(lowest_num, highest_num)
while True:
    print("Please enter number between 1 and 100!")
    number_guesses += 1
    guess_num = int(input("Enter guess_number: "))
    if guess_num > answer:
        print("Too high. Try again...!")
    elif guess_num < answer:
        print("Too Low. Try again...!")
    elif guess_num == answer:
        print(f"Correct!. The answer is {answer}")
        break
    else:
        print("Please enter the number between 1 and 100!")

print(f"The Correct answer is {answer}")
print(f"Number of Guess is {number_guesses}")

