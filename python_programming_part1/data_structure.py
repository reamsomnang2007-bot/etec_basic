datas = ["programming", "networking", "database", "web development"]
def menu():
    print("----------( Menu )----------")
    print("[1]. Add Data")
    print("[2]. Output Datas")
    print("[3]. Update Data")
    print("[4]. Delete Data")
    print("[5]. Exit")
    print("----------------------------")


while True:
    menu()
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print("----------( Add Data )----------")
            data = input("Enter your data: ")
            datas.append(data)
            print("Data added successfully!")
        case 2:
            print("----------( Output Datas )----------")
            if len(datas) == 0:
                print("No data available!")
            else:
                for i in range(len(datas)):
                    print(f"{i + 1}. {datas[i]}")
            print("----------------------------------")
        case 3:
            print("----------( Update Data )----------")
            if len(datas) == 0:
                print("No data available!")
            else:
                for i in range(len(datas)):
                    print(f"{i + 1}. {datas[i]}")
                index = int(input("Enter the index of the data to update: "))
                new_data = input("Enter the new data: ")
                datas[index - 1] = new_data
                print("Data updated successfully!")
        case 4:
            print("----------( Delete Data )----------")
            if len(datas) == 0:
                print("No data available!")
            else:
                for i in range(len(datas)):
                    print(f"{i + 1}. {datas[i]}")
                index = int(input("Enter the index of the data to delete: "))
                datas.pop(index - 1)
                print("Data deleted successfully!")
        case 5:
            print("Exit program...")
            break
