import sqlite3
import json

def create_table(): 
    try:
        cursor.execute('''
            CREATE TABLE client (
                name varchar(128),
                lastname varchar(128),
                age integer 
            )
        ''')
        print("Таблица 'client' успешно создана.")
    except sqlite3.OperationalError:
        print("Таблица 'client' уже существует.")

def add_client(client_name, client_lastname, client_age):
    cursor.execute('''SELECT * FROM client WHERE name=? AND lastname=?''', (client_name, client_lastname))
    if cursor.fetchone():
        return
    cursor.execute('''
        INSERT INTO client (name, lastname, age)
            VALUES (?, ?, ?)
    ''', [client_name, client_lastname, client_age])
    conn.commit() 

def json_add_client(path):
    with open(path, 'r', encoding='UTF-8') as f:
        d = json.load(f)
        for i in d:
            lst = []
            for j in i:
                lst.append(i[j])
            cursor.execute('''SELECT * FROM client WHERE name=? AND lastname=?''', (lst[0], lst[1]))
            if cursor.fetchone():
                return
            cursor.execute('''
                INSERT INTO client (name, lastname, age)
                VALUES (?, ?, ?)
            ''', lst)
            conn.commit()

def avg_client_age():
    cursor.execute('''SELECT avg(age) FROM client''')
    return cursor.fetchone()

# def get_client():
#     cursor.execute('''SELECT name, lastname, age FROM client''')
#     return cursor.fetchall()

conn = sqlite3.connect('database.db') 
cursor = conn.cursor()                

create_table()

add_client('Мари', 'Хлюстова', 41)
add_client('Иван', 'Родионов', 34)
add_client('Петр', 'Смирнов', 18)

json_add_client('data.json')

avg_age = round(avg_client_age()[0], 1)
print(f'Средний возраст клиентов {avg_age} лет')

# for row in get_client():
#     print(row)