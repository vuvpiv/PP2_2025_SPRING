import psycopg2
# Подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    dbname="phonebook",
    user="postgres",
    password="159357Aa@"  
)
cur = conn.cursor()
import json
def insert_many():
    users = [
        {"name": "Aru", "surname": "Zhumabek", "phone": "87006667788"},
        {"name": "Dias", "surname": "Sabitov", "phone": "87005554433"},
        {"name": "Kamila", "surname": "Asylbek", "phone": "87004443322"}
    ]

    cur.execute("CALL insert_many_users(%s);", [json.dumps(users)])
    conn.commit()
    print("Users inserted/updated successfully.\n")
# 1. Создание таблицы через SQL
def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            user_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            surname VARCHAR(255) NOT NULL,
            phone VARCHAR(255) NOT NULL
        );
    """)
    conn.commit()

# 2. Вставка или обновление пользователя через SQL-процедуру
def insert_or_update():
    name = input("Name: ")
    surname = input("Surname: ")
    phone = input("Phone: ")
    cur.execute("CALL insert_or_update_user(%s, %s, %s);", (name, surname, phone))
    conn.commit()

# 3. Показать все записи
def show_all():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)
def search_by_pattern():
    pattern = input("Enter search pattern (name, surname, or phone): ")
    query = f"SELECT * FROM search_phonebook('{pattern}');"
    cur.execute(query)
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No matches found.")

# Создаём таблицу, если её ещё нет
create_table()

# Главное меню
while True:
    print("""
    --- PhoneBook Menu ---
    1. Insert or update user
    2. Show all users
    3. Insert many users 
    4. Search by pattern
    5. Exit
    """)
    choice = input("Choose an option: ")

    if choice == "1":
        insert_or_update()
    elif choice == "2":
        show_all()
    elif choice == "3":
        insert_many()
    elif choice == "4":
        search_by_pattern()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
# Закрываем соединение
cur.close()
conn.close()
