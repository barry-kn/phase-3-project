import Create_data

MENU_PROMPT = """
--Cofee Bean App --
please chose one of these option:

1)Add a new bean.
2)See all beans.
3)Find a bean by name.
4)See which preparation methord is best for a bean.
5)Exit.
Your selection:"""




def menu():
    connection = Create_data.connect()
    Create_data.creat_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "5":
        print(user_input)

menu()