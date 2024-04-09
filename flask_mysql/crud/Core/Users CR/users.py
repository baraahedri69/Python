from server import mysql

class Users:
    @staticmethod
    def get_all_users():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM table1")
        users = cur.fetchall()
        cur.close()
        return users

    @staticmethod
    def create_user(first_name, last_name, email):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO table1 (first_name, last_name, email, created_at) VALUES (%s, %s, %s, NOW())", (first_name, last_name, email))
        mysql.connection.commit()
        cur.close()
