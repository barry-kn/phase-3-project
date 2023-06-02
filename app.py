import Create_data

MENU_PROMPT = """
--  BEANS IN KENYA  --
Please choose one of these options:

1) Add a new bean.
2) See all beans.
3) Find a bean by name.
4) See which preparation method is best for a bean.
5) Delete a bean.
6) Exit.
Your selection: """


def menu():
    session = Create_data.connect()

    while (user_input := input(MENU_PROMPT)) != "6":
        if user_input == "1":
            prompt_add_new_bean(session)
            
        elif user_input == "2":
            prompt_see_all_beans(session)

        elif user_input == "3":
            prompt_find_bean(session)

        elif user_input == "4":
            prompt_find_best_method(session)

        elif user_input == "5":
            prompt_delete_bean(session)

        else:
            print("INVALID INPUT. PLEASE TRY AGAIN.")


def prompt_add_new_bean(session):
    name = input("Enter bean name: ")
    method = input("Enter preparation method: ")
    rating = int(input("Enter rating score (0-100): "))

    Create_data.add_bean(session, name, method, rating)
    print("Bean added successfully!")


def prompt_see_all_beans(session):
    beans = Create_data.get_all_beans(session)

    if not beans:
        print("No beans found.")
    else:
        for bean in beans:
            print(f"{bean.name} ({bean.method}) - {bean.rating}/100")


def prompt_find_bean(session):
    name = input("Enter bean name to find: ")
    beans = Create_data.get_beans_by_name(session, name)

    if not beans:
        print("No beans found.")
    else:
        for bean in beans:
            print(f"{bean.name} ({bean.method}) - {bean.rating}/100")


def prompt_find_best_method(session):
    name = input("Enter bean name to find: ")

    
    best_method = Create_data.get_best_preparation_for_bean(session, name)

    if not best_method:
        print("Bean not found.")
    else:
        print(f"The best preparation method for {name} is: {best_method.method}.")


def prompt_delete_bean(session):
    name = input("Enter bean name to delete: ")
    beans = Create_data.get_beans_by_name(session, name)

    if not beans:
        print("Bean not found.")
    else:
        for index, bean in enumerate(beans, start=1):
            print(f"{index}) {bean.name} ({bean.method}) - {bean.rating}/100")

        choice = input("Enter the number corresponding to the bean you want to delete: ")
        try:
            index = int(choice) - 1
            if 0 <= index < len(beans):
                bean = beans[index]
                Create_data.delete_bean(session, bean.id)
                print("Bean deleted successfully!")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid choice.")


menu()
