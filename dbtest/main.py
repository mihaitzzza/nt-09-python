import MySQLdb

users = [
    {
        'first_name': 'Ion',
        'last_name': 'Iliescu',
        'email': 'a1@gmail.com',
    },
    {
        'first_name': 'George',
        'last_name': 'Daniel',
        'email': 'a2@gmail.com',
    }
]

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        database='nt_09_python',
        user='root',
        password='Mihai10!',
    )

    cursor = db.cursor()

    for user in users:
        cursor.execute("""
            INSERT IGNORE INTO `users`(first_name, last_name, email) VALUES(%s, %s, %s)
        """, (user['first_name'], user['last_name'], user['email']))

    db.commit()

    cursor.execute("SELECT id, email, first_name, last_name FROM `users`;")
    db_users = cursor.fetchall()
    print('db_users', db_users)

    users_from_db_list = [
        dict(zip(['id', 'email', 'first_name', 'last_name'], user))
        for user in db_users
    ]

    print('users_from_db_list', users_from_db_list)
