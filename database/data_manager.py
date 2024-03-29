from database.connection import connection_handler
import bcrypt


@connection_handler
def register_user(cursor, form_data):
    username = form_data.get('username')
    raw_password = form_data.get('password')
    hashed_password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())

    sql_query = 'insert into users(username, password) values (%(username)s, %(password)s);'

    cursor.execute(sql_query, {'username': username, 'password': hashed_password.decode('utf-8')})


@connection_handler
def get_user(cursor, username):
    sql_query = 'select * from users where username=%(username)s;'

    cursor.execute(sql_query, {'username': username})

    return cursor.fetchone()