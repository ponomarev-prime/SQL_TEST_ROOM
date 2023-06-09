import psycopg2
import random
from datetime import datetime
import base64
from faker import Faker

# Количество пользователей
number_of_users = 50

# INIT
fake = Faker()

# Параметры подключения к базе данных
host = "postgres"
database = "mydatabase"
user = "postgres"
password = "postgres"

# Подключение к базе данных
connection = psycopg2.connect(host=host, database=database, user=user, password=password)
cursor = connection.cursor()

# Генерация и вставка случайных записей
for _ in range(number_of_users):
    name = fake.name()
    age = random.randint(18, 65)
    email = name.lower().replace(' ', '_') + "@example.com"
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    number = random.randint(100000, 999999)
    description = fake.text().replace("\n", "")
    key = base64.b64encode((name + str(number)).encode()).decode()

    query = """
    INSERT INTO users (name, age, email, created_at, number, description, key)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (name, age, email, created_at, number, description, key)

    cursor.execute(query, values)

# Фиксация изменений и закрытие соединения
connection.commit()
cursor.close()
connection.close()

print("Записи успешно добавлены в таблицу.")
