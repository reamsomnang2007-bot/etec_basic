while True:
    print("----------{ Option }----------")
    print("[1]. Register Account")
    print("[2]. Login Account")
    print("[3]. Exit")
    print("------------------------------")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("-----{ Register }-----")
        user_name = input("User_name: ")
        email = input("Email: ")
        password = input("Password: ")
        print("Register successfully!")
        print("----------------------")
    elif choice == 2:
        print("-----{ Login }-----")
        login_email = input("Enter Email to Login: ")
        login_password = input("Enter Password to Login: ")
        if login_email == email and password == login_password:
            print("Login Successfully...!")
        elif login_email != email and password == login_password:
            print("Wrong email!. Try again...")
        elif login_email == email and password != login_password:
            print("Wrong password!. Try again...")
        else:
            print("Don't have this account!")
        print("----------------------")
    elif choice == 3:
        print("Exit program...!")
        break
    else:
        print("Invalid choice. Please enter only number 1-3!")