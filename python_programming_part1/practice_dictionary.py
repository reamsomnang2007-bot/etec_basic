datas = [
    {
        "id": 1,
        "name": "Chanda",
        "gender": "Male",
        "age": 29
    },
    {
        "id": 2,
        "name": "Sovann",
        "gender": "Male",
        "age": 19
    },
    {
        "id": 3,
        "name": "Makara",
        "gender": "Male",
        "age": 28
    }
]
def menu():
    print("-----[ Menu ]-----")
    print("[1]. Add data")
    print("[2]. Output datas")
    print("[3]. Update data")
    print("[4]. Delete data")
    print("[5]. Exit")
    print("------------------")

while True:
    menu()
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print("-----[ Add data ]-----")
            id = int(input("Enter ID: "))
            name = input("Enter name: ")
            gender = input("Enter gender: ")
            age = int(input("Enter age: "))
            datas.append({
                "id": id,
                "name": name,
                "gender": gender,
                "age": age
            })
            print("Add data successfully!")
            print("----------------------")
        case 2:
            print("-----[ Output datas ]-----")
            for data in datas:
                print("-----[ Data ]-----")
                for key, value in data.items():
                    print(f"{key}: {value}")
                print("------------------")
        case 3:
            print("-----[ Update data ]-----")
            update_id = int(input("Enter the ID for Update: "))
            for data in datas:
                if data['id'] == update_id:
                    data['name'] = input("Enter new name: ")
                    data['gender'] = input("Enter new gender: ")
                    data['age'] = int(input("Enter new age: "))
                    break
            print("Update data successfully!")
            print("------------------------")
        case 4:
            print("-----[ Delete data ]-----")
            print("[1]. Delete by ID")
            print("[2]. Delete by Name")
            print("-------------------------")
            delete_choice = int(input("Enter your choice: "))
            match delete_choice:
                case 1:
                    print("-----[ Delete by ID ]-----")
                    delete_id = int(input("Enter the ID to delete: "))
                    for data in datas:
                        if data['id'] == delete_id:
                            datas.remove(data)
                            break
                    print("Delete data successfully!")
                    print("-------------------------")
                case 2:
                    print("-----[ Delete by Name ]-----")
                    delete_name = input("Enter the Name to delete: ")
                    for data in datas:
                        if data['name'] == delete_name:
                            datas.remove(data)
                            break
                    print("Delete data successfully!")
                    print("---------------------------")
        case 5:
            print("Exiting the program...")
            break
        
