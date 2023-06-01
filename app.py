import Create_data

MENU_PROMPT = """
-- Coffee Bean App --
Please choose one of these options:

1) Add a new bean.
2) See all beans.
3) Find a bean by name.
4) See which preparation method is best for a bean.
5) Delete a bean.
6) Exit.
Your selection: """


def menu():
    connection = Create_data.connect()
    Create_data.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "6":
        if user_input == "1":
            prompt_add_new_bean(connection)
            
        elif user_input == "2":
            prompt_see_all_beans(connection)

        elif user_input == "3":
            prompt_find_bean(connection)

        elif user_input == "4":
            prompt_find_best_method(connection)

        elif user_input == "5":
            prompt_delete_bean(connection)

        else:
            print("INVALID INPUT. PLEASE TRY AGAIN.")


def prompt_add_new_bean(connection):
    name = input("Enter bean name: ")
    method = input("Enter preparation method: ")
    rating = int(input("Enter rating score (0-100): "))

    Create_data.add_bean(connection, name, method, rating)
    print("Bean added successfully!")


def prompt_see_all_beans(connection):
    beans = Create_data.get_all_beans(connection)

    if not beans:
        print("No beans found.")
    else:
        for bean in beans:
            print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")


def prompt_find_bean(connection):
    name = input("Enter bean name to find: ")
    beans = Create_data.get_beans_by_name(connection, name)

    if not beans:
        print("No beans found.")
    else:
        for bean in beans:
            print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")


def prompt_find_best_method(connection):
    name = input("Enter bean name to find: ")
    best_method = Create_data.get_best_preparation_for_bean(connection, name)

    if not best_method:
        print("Bean not found.")
    else:
        print(f"The best preparation method for {name} is: {best_method[2]}.")


def prompt_delete_bean(connection):
    name = input("Enter bean name to delete: ")
    beans = Create_data.get_beans_by_name(connection, name)

    if not beans:
        print("Bean not found.")
    else:
        for index, bean in enumerate(beans, start=1):
            print(f"{index}) {bean[1]} ({bean[2]}) - {bean[3]}/100")

        choice = input("Enter the number corresponding to the bean you want to delete: ")
        try:
            index = int(choice) - 1
            if 0 <= index < len(beans):
                bean = beans[index]
                Create_data.delete_bean(connection, bean[0])
                print("Bean deleted successfully!")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid choice.")


menu()
