# import our get connection function
from utils import dbconfig


# function that adds a new reimbursement to the database
def create_reimbursement(employee_id, amount, reason, date_created, manager_id=None, review_comments=None,
                         date_reviewed=None, status='pending'):
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = "INSERT INTO reimbursements VALUES (default, ?, ?, ?, ?, ?, ?, ?, ?)"
        # execute our query and commit the changes to the database
        cursor.execute(query, employee_id, amount, reason, date_created, manager_id, review_comments,
                       date_reviewed, status)
        cursor.commit()
    finally:
        # close our database connection
        connection.close()


# function that pulls all of our reimbursements from the database
def get_all_reimbursements(employee_id=None, manager_id=None):
    # create result variable
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string
        if employee_id is not None:
            query = "SELECT * FROM reimbursements WHERE employee_id = ? ORDER BY reimbursement_id"
            # execute our query
            cursor.execute(query, employee_id)
        elif manager_id is not None:
            query = "SELECT * FROM reimbursements WHERE manager_id = ? ORDER BY reimbursement_id"
            # execute our query
            cursor.execute(query, manager_id)
        else:
            query = "SELECT * FROM reimbursements ORDER BY reimbursement_id"
            # execute our query
            cursor.execute(query)

        # use cursor to fetch the results of the query
        result = cursor.fetchall()
    finally:
        # close our database connection
        connection.close()
        # return the result
        return result


def get_pending_reviews():
    # create result variable
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string
        query = "SELECT * FROM reimbursements WHERE status = 'pending' ORDER BY reimbursement_id"
        # execute our query
        cursor.execute(query)
        # use cursor to fetch the results of the query
        result = cursor.fetchall()
    finally:
        # close our database connection
        connection.close()
        # return the result
        return result


def get_past_reimbursements():
    # create result variable
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string
        query = "SELECT * FROM reimbursements WHERE status = 'approved'"
        # execute our query
        cursor.execute(query)
        # use cursor to fetch the results of the query
        result = cursor.fetchall()
    finally:
        # close our database connection
        connection.close()
        # return the result
        return result


# function that pulls a specific reimbursement from the database
def get_reimbursement(reimbursement_id):
    # create result variable
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = "SELECT * FROM reimbursements WHERE reimbursement_id = ?"
        # execute our query
        cursor.execute(query, reimbursement_id)
        # fetch the results of the query
        result = cursor.fetchone()
    finally:
        # close our database connection
        connection.close()
        # return the result
        return result


# function that updates the information of an existing reimbursement
def update_reimbursement(reimbursement_id, amount, reason, date_created):
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = """UPDATE reimbursements SET amount = ?, reason = ?, date_created = ?, 
                status = 'pending' WHERE reimbursement_id = ?"""
        # execute our query and commit the changes to the database
        cursor.execute(query, amount, reason, date_created, reimbursement_id)
        cursor.commit()
    finally:
        # close our database connection
        connection.close()


def review_reimbursement(reimbursement_id, manager_id, review_comments, date_reviewed, status='pending'):
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = """UPDATE reimbursements SET manager_id = ?, review_comments = ?, date_reviewed = ?, status = ? 
                WHERE reimbursement_id = ?"""
        # execute our query and commit the changes to the database
        cursor.execute(query, manager_id, review_comments, date_reviewed, status, reimbursement_id)
        cursor.commit()
    finally:
        # close our database connection
        connection.close()


# function that deletes a reimbursement from the database
def delete_reimbursement(reimbursement_id):
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string using parameterization to protect against SQL injection
        query = "DELETE FROM reimbursements WHERE reimbursement_id = ?"
        # execute our query and commit the changes to the database
        cursor.execute(query, reimbursement_id)
        cursor.commit()
    finally:
        # close our database connection
        connection.close()


def get_biggest_single_spender():
    # create result variable
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string
        query = """SELECT user_first_name, user_last_name FROM users WHERE user_id =
                (SELECT employee_id FROM reimbursements WHERE amount =
                (SELECT MAX (amount) FROM reimbursements WHERE status = 'approved') LIMIT 1)"""
        # execute our query
        cursor.execute(query)
        # fetch the results of the query
        result = cursor.fetchone()
    finally:
        # close our database connection
        connection.close()
        # return the result
        return result


def get_biggest_total_spender():
    # create result variable
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string
        query = """SELECT user_first_name, user_last_name FROM users WHERE user_id = (SELECT employee_id FROM 
                (SELECT employee_id, SUM(amount) AS amount_sum FROM reimbursements WHERE status = 'approved' 
                GROUP BY employee_id ORDER BY amount_sum DESC LIMIT 1) AS employee)"""
        # execute our query
        cursor.execute(query)
        # fetch the results of the query
        result = cursor.fetchone()
    finally:
        # close our database connection
        connection.close()
        # return the result
        return result


def get_average_amount():
    # create result variable
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string
        query = "SELECT AVG (amount::numeric) FROM reimbursements WHERE status = 'approved'"
        # execute our query
        cursor.execute(query)
        # fetch the results of the query
        result = cursor.fetchval()
    finally:
        # close our database connection
        connection.close()
        # return the result
        return result


def get_highest_amount():
    # create result variable
    result = None
    try:
        # set up a new database connection and cursor
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        # create query string
        query = "SELECT MAX (amount) FROM reimbursements WHERE status = 'approved'"
        # execute our query
        cursor.execute(query)
        # fetch the results of the query
        result = cursor.fetchval()
    finally:
        # close our database connection
        connection.close()
        # return the result
        return result
