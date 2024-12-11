# db.py
import os
import pymysql
from flask import jsonify

db_host = os.environ.get('CLOUD_SQL_HOST')
db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    try:
        conn = pymysql.connect(
            host=db_host,
            port=3306,
            user=db_user,
            password=db_password,
            db=db_name,
        )
        return conn
    except pymysql.OperationalError as e:
        return jsonify(f"Error connecting to the database: {e}")
        # return None  # Return None or handle the error as needed


def get():
    conn = open_connection()
    if conn is None:
        # Handle the case where the connection failed
        return {"error": "Database connection failed"}, 500
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users")  # Example query
        results = cursor.fetchall()

    conn.close()  # Don't forget to close the connection
    return jsonify(results)


def create(user):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO users (name, age, sex) VALUES(%s, %s, %s)',
                       (user["name"], user["age"], user["sex"]))
    conn.commit()
    conn.close()


def save_topic_message(message):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO topic_messages (topic_message) VALUES(%s)',
                       (message.data.decode("utf-8")))
    conn.commit()
    conn.close()
