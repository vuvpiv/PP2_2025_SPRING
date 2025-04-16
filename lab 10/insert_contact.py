import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    dbname="phonebook",
    user="postgres",
    password="159357Aa@",  # ← сюда впиши свой пароль от PostgreSQL
    port="5432"
)

cur = conn.cursor()

# Добавление нового контакта
name = input("Enter name: ")
phone = input("Enter phone: ")

cur.execute(
    "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
    (name, phone)
)

conn.commit()
print("Contact added successfully!")

cur.close()
conn.close()
