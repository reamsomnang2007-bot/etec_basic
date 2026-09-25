
def menu():
    print("----------{ Menu }----------")
    print("[1]. Register")
    print("[2]. Login")
    print("[3]. Exit")
    print("----------------------------")

def register():
    global user_name, email, password
    print("----------{ Register }----------")
    user_name = input("Enter your username: ")
    email = input("Enter your email: ")
    while True:
        if "@" in email and "." in email:
            break
        else:
            print("Invalid email format! Please try again.")
            email = input("Enter your email: ")
    while(True):
        if len(password) < 8:
            print("Password must be at greater than 8. Please try again.")
            password = input("Enter your password: ")
        else:
            break
    print(f"'{user_name}' Register successful!")
    print("-------------------------------")
def login():
    print("----------{ Login }----------")
    email_login = input("Enter your email: ")
    password_login = input("Enter your password: ")
    if email_login == email and password_login == password:
        print(f"'{user_name}' Login successful!")
    else:
        print("Login failed! Please check your email and password.")
def main():
    while True:
        menu()
        choice = int(input("Enter your choice: "))
        if(choice == 1):
            register()
        elif(choice == 2):
            login()
        elif(choice == 3):
            print("Exit program...")
            break
        else:
            print("Invalid choice! Please try again.")
main()
