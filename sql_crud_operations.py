import sqlite3


connection = sqlite3.connect('example.db')


cursor = connection.cursor()


def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    connection.commit()

# Create 
def create_user(name, age):
    cursor.execute('''
        INSERT INTO users (name, age) VALUES (?, ?)
    ''', (name, age))
    connection.commit()

# Read 
def read_users():
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()

# Update 
def update_user(user_id, name, age):
    cursor.execute('''
        UPDATE users
        SET name = ?, age = ?
        WHERE id = ?
    ''', (name, age, user_id))
    connection.commit()

# Delete 
def delete_user(user_id):
    cursor.execute('''
        DELETE FROM users WHERE id = ?
    ''', (user_id,))
    connection.commit()


if __name__ == '__main__':
    create_table()
    create_user('Alice', 30)
    create_user('Bob', 25)
    
    print('Users after creation:')
    print(read_users())

    update_user(1, 'Alice Smith', 31)
    print('Users after update:')
    print(read_users())

    delete_user(2)
    print('Users after deletion:')
    print(read_users())


connection.close()
