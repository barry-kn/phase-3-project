import Create_data

def menu():
    connection = Create_data.connect()
    Create_data.creat_table(connection)