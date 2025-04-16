import csv
import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",        
    password="159357Aa@"   
)
cur = conn.cursor()

# Открытие CSV-файла и вставка данных
with open('contacts.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['name']
        phone = row['phone']
        cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))

# Сохранение изменений и закрытие соединения
conn.commit()
cur.close()
conn.close()

print("Данные успешно загружены из CSV!")
