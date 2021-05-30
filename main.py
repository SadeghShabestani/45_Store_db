from sqlite3 import connect


class Database:
    connect = connect("store.db")
    cursor = connect.cursor()

    @staticmethod
    def show_all():
        Database.cursor.execute("SELECT * FROM Products")
        result = Database.cursor.fetchall()
        print(result)
        # Database.connect.close()

    @staticmethod
    def insert():
        name = input("Enter Name: ")
        price = input("Enter Price: ")
        count = input("Enter Count: ")
        Database.cursor.execute(f"INSERT INTO Products(name , price,count) VALUES ('{name}',{price},{count})")
        Database.cursor.execute("SELECT * FROM Products")
        Database.connect.commit()
        result = Database.cursor.fetchall()
        print(result)
        # Database.connect.close()

    @staticmethod
    def update():
        name = input("Enter Product Name: ")
        price = input("Enter Price: ")
        count = input("Enter Count: ")
        Database.cursor.execute(
            f"UPDATE Products SET name = '{name}' , price = {price} , count = {count} WHERE name = 'rice'")
        Database.cursor.execute("SELECT * FROM Products")
        Database.connect.commit()
        result = Database.cursor.fetchall()
        print(result)
        # Database.connect.close()

    @staticmethod
    def delete():
        name = input("Enter Product Name: ")
        Database.cursor.execute(f"DELETE FROM Products WHERE name = 'pofak' ")
        Database.cursor.execute("SELECT * FROM Products")
        Database.connect.commit()
        result = Database.cursor.fetchall()
        print(result)
        # Database.connect.close()


def show_menu():
    menu = ["1_Show Products", "2_Insert Products", "3_Update Products", "4_Delete Products", "5_Exit"]
    for item in menu:
        print(item)


while True:
    show_menu()
    user = int(input("\nEnter Choice: "))
    if user == 1:
        Database.show_all()

    elif user == 2:
        Database.insert()

    elif user == 3:
        Database.update()

    elif user == 4:
        Database.delete()

    elif user == 5:
        exit()
