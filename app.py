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
            method = input ("enter how u have prepared it: ")
            rating = int (input("enter your rating (0-100): "))
            
            Create_data.add_bean(connection, name ,method, rating)
            
        elif user_input == "2":
            beans = Create_data.get_all_beans(connection)

            for bean in beans:
                print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100 ")
        elif user_input == "3":
            name = input ("enter bean by name to find:")
            bean = Create_data.get_beans_by_name(connection, name)


            for bean in beans:
                print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100 ")
            



        elif user_input == "4":
            name = input("enter bean name find:")
            best_method =Create_data.get_best_preparation_for_bean(connection,name)

            print(f"the best preparation method for {name} is: { best_method[2]}")
            


        else:
            print("INVALID INPUT TY AGAIN")




def prompt_add_new_bean(connection):
    name = input("enter bean name : ")
    method = input("enter how you have prepared it: ")
    rating = int(input("enter your rating score (0-100): "))


    Create_data.add_bean(connection, name, method, rating)


def prompt_see_all_bean(connection):
    beans =  Create_data.get_all_beans(connection)

    for bean in beans:
        print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")


def prompt_find_bean(connection):
    name = input("enter bean name to find: ")
    beans = Create_data.get_beans_by_name(connection, name)

    for bean in beans:
        print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")

def prompt_find_best_method(connection):
    name = input("enter bean name to find: ")
    beast_method = Create_data.get_best_preparation_for_bean(connection, name)

    print(f"the best preparation method for {name} is: {best_method[2]}.")

menu()
