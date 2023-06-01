import Create_data

MENU_PROMPT = """
-- Coffee Bean App --
Please choose one of these options:

1) Add a new bean.
2) See all beans.
3) Find a bean by name.
4) See which preparation method is best for a bean.
5) Exit.
Your selection: """


def menu():
    connection = Create_data.connect()
    Create_data.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "5":
        print(user_input)
        if user_input == "1":
            name = input("enter bean name: ")
            method = input ("enter how u have prepared it")
            rating = int (input("enter your rating (0-100)"))
            
            Create_data.add_bean(connection, name ,method, rating)
            
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            print("INVALID INPUT TY AGAIN")

menu()
