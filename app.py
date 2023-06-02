import Create_data

MENU_PROMPT = """
-- Coffee Bean App --
Please choose one of these options:

1) Add a new bean.
2) See all beans.
3) Find a bean by name.
4) See which preparation method is best for a bean.
5) Delete a bean.
6) Add a new farmer.
7) Exit.
Your selection: """


def menu():
    session = Create_data.connect()

    while True:
        user_input = input(MENU_PROMPT)

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

        elif user_input == "6":
            prompt_add_new_farmer(session)

        elif user_input == "7":
            break

        else:
            print("INVALID INPUT. PLEASE TRY AGAIN.")


def prompt_add_new_bean(session):
    name = input("Enter bean name: ")
    method = input("Enter preparation method: ")
    rating = int(input("Enter rating score (0-100): "))

    Create_data.add_bean(session, name, method, rating)
    print("Bean added successfully!")

def prompt_add_new_farmer(session):
    name = input("Enter farmer name: ")
    area = input("Enter area: ")
    while True:
        phone = input("Enter phone number: ")
        try:
            phone = int(phone)
            break
        except ValueError:
            print("Invalid phone number. Please enter a valid integer.")
    Create_data.add_farmer(session, name, area, phone)
    print("Farmer added successfully!")


def prompt_see_all_beans(session):
    beans = Create_data.get_all_beans(session)
    if beans:
        print("List of all beans:")
        for bean in beans:
            print(f"Name: {bean.name}, Method: {bean.method}, Rating: {bean.rating}")
    else:
        print("No beans found.")


def prompt_find_bean(session):
    name = input("Enter bean name: ")
    bean = Create_data.find_bean_by_name(session, name)
    if bean:
        print(f"Bean found - Name: {bean.name}, Method: {bean.method}, Rating: {bean.rating}")
    else:
        print("Bean not found.")


def prompt_find_best_method(session):
    name = input("Enter bean name: ")
    method = Create_data.find_best_preparation_method(session, name)
    if method:
        print(f"The best preparation method for {name} is {method}.")
    else:
        print("Bean not found.")


def prompt_delete_bean(session):
    name = input("Enter bean name: ")
    bean = Create_data.find_bean_by_name(session, name)
    if bean:
        Create_data.delete_bean(session, bean)
        print(f"Bean {name} deleted successfully!")
    else:
        print("Bean not found.")

menu()
