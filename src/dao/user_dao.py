# import our get connection function
from utils import dbconfig


# function that adds a new user to the database
def create_user(user_first_name, user_last_name, user_email, user_manager_privilege):
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = "INSERT INTO users VALUES (default, ?, ?, ?, ?)"
        # execute our query and commit the changes to the database
        cursor.execute(query, user_first_name, user_last_name, user_email, user_manager_privilege)
        cursor.commit()
    finally:
        # close our database connection
        connection.close()


# function that adds a new user login to the database
def create_login(user_id, user_email, user_password):
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = "INSERT INTO user_logins VALUES (?, ?, ?)"
        # execute our query and commit the changes to the database
        cursor.execute(query, user_id, user_email, user_password)
        cursor.commit()
    finally:
        # close our database connection
        connection.close()


# function that pulls all of our users from the database
def get_all_users():
    # create result variable
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string
        query = "SELECT * FROM users"
        # execute our query
        cursor.execute(query)
        # use cursor to fetch the results of the query
        result = cursor.fetchall()
    finally:
        # close our database connection
        connection.close()
        # return the result
        return result


# function that pulls a specific user from the database
def get_user(user_id):
    # create result variable
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = f"SELECT * FROM users WHERE user_id = ?"
        # execute our query
        cursor.execute(query, user_id)
        # fetch the results of the query
        result = cursor.fetchone()
    finally:
        # close our database connection
        connection.close()
        # return the result
        return result


# function that updates the information of an existing user
def update_user(user_id, user_first_name, user_last_name, user_email, user_manager_privilege):
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = """UPDATE users SET user_first_name = ?, user_last_name = ?, user_email = ?, manager_privilege = ? 
                WHERE user_id = ?"""
        # execute our query and commit the changes to the database
        cursor.execute(query, user_first_name, user_last_name, user_email, user_manager_privilege, user_id)
        cursor.commit()
    finally:
        # close our database connection
        connection.close()


# function that deletes a user from the database
def delete_user(user_id):
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = "DELETE FROM users WHERE user_id = ?"
        # execute our query and commit the changes to the database
        cursor.execute(query, user_id)
        cursor.commit()
    finally:
        # close our database connection
        connection.close()


# function for checking if a user email already exists in the database
# also for retrieving the id associated with an email address
def check_email(email):
    # create result variable
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = "SELECT user_id FROM users WHERE user_email = ?"
        # execute our query
        cursor.execute(query, email)
        # fetch the results of the query
        result = cursor.fetchval()
    finally:
        # close our database connection
        connection.close()
        # return the result
        if result is None:
            return result
        else:
            return result


# function that returns the hashed password associated with a given email address
def check_password(email):
    # create result variable
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = "SELECT user_password FROM user_logins WHERE user_email = ?"
        # execute our query
        cursor.execute(query, email)
        # fetch the results of the query
        result = cursor.fetchval()
    finally:
        # close our database connection
        connection.close()
        # return the result
        if result is None:
            return result
        else:
            return result
