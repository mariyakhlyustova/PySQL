import sqlite3

def add_user(user_name, user_lastname):
    cursor.execute('''
        INSERT INTO users (name, lastname)
            values (?, ?)
    ''', [user_name,user_lastname])
    conn.commit() 

def del_user(user_name):
    cursor.execute('''
        delete from  users 
        where name = ?
    ''', [user_name])
    conn.commit()

def get_users():
    cursor.execute('select name, lastname from users')
    return cursor.fetchall()

def change_lastname(user_name, new_lastname):
    cursor.execute('''
        update  users set lastname = ?
        where name = ?
    ''', [new_lastname, user_name])
    conn.commit()

conn = sqlite3.connect('database.db') # подключение
cursor = conn.cursor()                # запрос

# cursor.execute('''
#     create table users(
#         name varchar(128),
#         lastname varchar(128)
#     )
# ''')

# execute -                            выполнение
# cursor.execute('''
#     INSERT INTO users (name, lastname)
#         values (?, ?)
# ''', ['Мария', 'Хлюстова'])

# add_user('Маруся', 'Хлюстова')
# add_user('Вася', 'Хлюстова')
# add_user('Петя', 'Хлюстова')

# del_user('Петя')

change_lastname('Вася', 'Петров')
# conn.commit()                          # фиксация
# cursor.execute('select * from users')

for row in get_users():
    print(row)