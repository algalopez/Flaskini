import mysql.connector
import logging

connection: mysql.connector.Connect


def connect_to_database():
    global connection
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="user",
            password="pass",
            database="flaskini"
        )
    except mysql.connector.Error as err:
        logging.error(err)


def disconnect_from_database():
    connection.close()


def execute(*commands):
    cursor = connection.cursor()
    for command in commands:
        cursor.execute(command)
    connection.commit()
    cursor.close()


def query_all(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return result


def query_one(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    return result


def prepare_database(before, after):
    def inner_decorator(f):
        def wrapped(*args, **kwargs):
            connect_to_database()
            execute(*before)
            try:
                response = f(*args, **kwargs)
            finally:
                execute(*after)
                disconnect_from_database()
            return response
        return wrapped
    return inner_decorator


def test_clean_database_helper():
    connect_to_database()
    execute('DELETE FROM list;')
    execute('DELETE FROM item;')
    disconnect_from_database()
