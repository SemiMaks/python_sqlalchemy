import psycopg2

from config import user, password, host, db_name, port

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port=port
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")

        # create a table
        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         """CREATE TABLE users(
        #         id serial PRIMARY KEY,
        #         first_name varchar(50) NOT NULL,
        #         nick_name varchar(50) NOT NULL);"""
        #     )
        #     print("[INFO] Table created successfully")

        # insert data in the table
        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         """INSERT INTO users(first_name, nick_name) VALUES
        #         ('Maksim', 'semimaks');"""
        #     )
        #     print("[INFO] Data was successfully inserted")

        # get data from a table
        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         """SELECT nick_name FROM users WHERE first_name = 'Maksim';"""
        #     )
        #     print(cursor.fetchone())

        # delete a table
        with connection.cursor() as cursor:
            cursor.execute(
                """DROP TABLE users;"""
            )
            print("[INFO] Table was deleted")

except Exception as _ex:
    print("[INFO Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
