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
            pass
            
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
