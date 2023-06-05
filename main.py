from Create_data import connect, Bean, Farmer

MENU_PROMPT = """
-- Prediction App --
Please choose one of these options:

1) User
2) Government
3) Farmer
4) Hotel
5) Exit
Your selection: """

def menu():
    session = connect()

    while True:
        user_input = input(MENU_PROMPT)

        if user_input == "1":
         user_menu(session)
            
        elif user_input == "2":
            pass
            

        elif user_input == "3":
            pass
            

        elif user_input == "4":
            pass
            

        elif user_input == "5":
            break

        else:
            print("INVALID INPUT. PLEASE TRY AGAIN.")

def user_menu(session):
    user_option = ""
    while user_option != "3":
        user_option = input("""
-- User Menu --
Please choose one of these options:

1) See all beans.
2) Rate a bean.
3) Go back to main menu.
Your selection: """)

        if user_option == "1":
            prompt_see_all_beans(session)

        elif user_option == "2":
            prompt_rate_bean(session)

        elif user_option == "3":
            break

        else:
            print("INVALID INPUT. PLEASE TRY AGAIN.")


def government_menu(session):
    government_option = ""
    while government_option != "2":
        government_option = input("""
-- Government Menu --
Please choose one of these options:

1) See all beans (sorted by rating in descending order).
2) Go back to main menu.
Your selection: """)

        if government_option == "1":
            prompt_see_all_beans(session, display_area=True)

        elif government_option == "2":
            break

        else:
            print("INVALID INPUT. PLEASE TRY AGAIN.")

