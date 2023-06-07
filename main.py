
from Create_data import connect, Bean, Farmer, Government
 

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
            government_menu(session)

        elif user_input == "3":
            farmer_menu(session)

        elif user_input == "4":
            hotel_menu(session)

        elif user_input == "5":
            break

        else:
            print("INVALID INPUT. PLEASE TRY AGAIN.")


############# UUUUUUUUUUUUUUUUUUU ##########

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
###### eeeeeeeeeee uuuuuuuuuuuuuuuu  #######################



################# GGGGGGGGGGGGGGGGGGG #################

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
            prompt_see_all_beans_government(session)

        elif government_option == "2":
            break

        else:
            print("INVALID INPUT. PLEASE TRY AGAIN.")

######### eeeeeeeeeeeeeeeeeeeeeeeeeee ###########



################# FFFFFFFFFFFFFFFFFFFFFFFFFF ####################

def farmer_menu(session):
    farmer_option = ""
    while farmer_option != "4":
        farmer_option = input("""
-- Farmer Menu --
Please choose one of these options:

1) Add a new bean.
2) Delete a farmer and their details.
3) Go back to the main menu.
Your selection: """)

        if farmer_option == "1":
            prompt_add_new_bean(session)

        elif farmer_option == "2":
            prompt_delete_farmer(session)

        elif farmer_option == "3":
            break

        else:
            print("INVALID INPUT. PLEASE TRY AGAIN.")

################ eeeeeeeeeeeeeeeeeeeeeeee #########################




########## HHHHHHHHHHHHHHHHHHHHHHHH ##################################

def hotel_menu(session):
    hotel_option = ""
    while hotel_option != "3":
        hotel_option = input("""
-- Hotel Menu --
Please choose one of these options:

1) Add method for a bean.
2) Go back to main menu.
Your selection: """)

        if hotel_option == "1":
            prompt_add_bean_method(session)

        elif hotel_option == "2":
            break

        else:
            print("INVALID INPUT. PLEASE TRY AGAIN.")

######## eeeeeeeeeeeeeeeeeeeeeeeeee ################################



############   111111111 uuuuuuuuuuuuu#############
def prompt_see_all_beans(session):
    beans = session.query(Bean).order_by(Bean.rating.desc()).all()
    if beans:
        print("List of all beans (sorted by rating in descending order):")
        for bean in beans:
            farmer = session.query(Farmer).filter_by(id=bean.farmer_id).first()
            if farmer:
                print(f"Bean: {bean.name}, Rating: {bean.rating}, Farmer's Area: {farmer.area}")
            else:
                print(f"Bean: {bean.name}, Rating: {bean.rating}, Farmer's Area: Unknown")
    else:
        print("No beans found.")
############# eeeeeeeeeeeeeeeeeeeeeeeeee ###############


############ 22222222222 uuuuuuuuuuuu ###########

def prompt_rate_bean(session):
    name = input("Enter bean name: ")
    rating = int(input("Enter rating score (0-100): "))

    bean = session.query(Bean).filter_by(name=name).first()
    if bean:
        bean.rating = rating
        session.commit()
        print("Bean rated successfully!")
    else:
        print("Bean not found.")
############ eeeeeeeeeeeeeeeeeeeeeeeee ###############



######### 11111111111111 ggggggggggggg #################

def prompt_see_all_beans_government(session):
    beans = session.query(Bean).order_by(Bean.rating.desc()).all()
    if beans:
        print("List of all beans (sorted by rating in descending order):")
        for bean in beans:
            farmer = session.query(Farmer).filter_by(id=bean.farmer_id).first()
            if farmer:
                print(f"Bean: {bean.name}, Rating: {bean.rating}, Farmer's Area: {farmer.area}")
                government = Government(bean_name=bean.name, rating=bean.rating, farmer_area=farmer.area)
                session.add(government)
                session.commit()
            else:
                print(f"Bean: {bean.name}, Rating: {bean.rating}, Farmer's Area: Unknown")
    else:
        print("No beans found.")
############ eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee ######################




######### 111111111111  ffffffffffffffffffff ##############
def prompt_add_new_bean(session):
    name = input("Enter bean name: ")
    farmer_id = int(input("Enter farmer ID: "))
    area = input("Enter farmer's area: ")
    phone_number = input("Enter your number: ")

    farmer = Farmer(id=farmer_id, area=area, phone_number=phone_number)
    session.add(farmer)
    session.commit()

    bean = Bean(name=name, farmer_id=farmer_id)
    session.add(bean)
    session.commit()
    print("Bean added successfully!")
####### eeeeeeeeeeeeeeeeeeeeeeeeeeeeee ##########################



def prompt_delete_farmer(session):
    farmer_id = int(input("Enter the ID of the farmer you want to delete: "))

    farmer = session.query(Farmer).filter_by(id=farmer_id).first()
    if farmer:
        beans = session.query(Bean).filter_by(farmer_id=farmer_id).all()
        for bean in beans:
            session.delete(bean)

        session.delete(farmer)
        session.commit()
        print("Farmer and their associated beans have been deleted successfully!")
    else:
        print("Farmer not found.")




#########   1111111111 hhhhhhhhhhhhhhh ##############################
def prompt_add_bean_method(session):
    name = input("Enter bean name: ")
    method = input("Enter preparation method: ")

    bean = session.query(Bean).filter_by(name=name).first()
    if bean:
        bean.method = method
        session.commit()
        print("Method added for the bean successfully!")
    else:
        print("Bean not found.")

######## eeeeeeeeeeeeeeeeeeeeeee ###################################


menu()