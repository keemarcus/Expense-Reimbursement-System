# import testing and mock functionality
import datetime
from unittest import mock, TestCase
# import our dao to test
from src.dao import reimbursement_dao as dao
# import database stuff
from utils import dbconfig
from pyodbc import connect


# we need to run this function to get a new mock connection everytime we need to access the test database
def make_mock_connection():
    mock_connection = connect("DRIVER=PostgreSQL UNICODE(x64);SERVER=localhost;PORT=5432;DATABASE=postgres;UID=postgres;PWD=password;Trusted_Connection=no;BoolsAsChar=0")
    dbconfig.get_connection = mock.Mock(return_value=mock_connection)


# this function is used to find the id of the most recent reimbursement in the database
def get_highest_id():
    # get a new mock connection
    make_mock_connection()
    # determine the largest id in the database
    connection = dbconfig.get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT MAX (reimbursement_id) FROM reimbursements")
    result = cursor.fetchone()
    if result[0] is None:
        return 0
    else:
        return result[0]


class ReimbursementDaoTests(TestCase):
    # test our create reimbursement function
    def test_create_reimbursement(self):
        # determine the highest current id
        reimbursement_id = get_highest_id()

        # get a new mock connection
        make_mock_connection()
        # execute the function
        dao.create_reimbursement(1, 0.00, 'reason', datetime.datetime(1997, 12, 6, 12, 0, 0))

        # retrieve the new reimbursement from the database
        make_mock_connection()
        reimbursement = dao.get_reimbursement(reimbursement_id + 1)

        # make sure that all the values are correct
        self.assertEqual(reimbursement[0], reimbursement_id + 1)
        self.assertEqual(reimbursement[1], 1)
        self.assertEqual(reimbursement[2], 0.00)
        self.assertEqual(reimbursement[3], 'reason')
        self.assertEqual(reimbursement[4], datetime.datetime(1997, 12, 6, 12, 0, 0))
        self.assertEqual(reimbursement[5], None)
        self.assertEqual(reimbursement[6], None)
        self.assertEqual(reimbursement[7], None)
        self.assertEqual(reimbursement[8], 'pending')

    # test our get_all_reimbursements function
    def test_get_all_reimbursements(self):
        # get a new mock connection
        make_mock_connection()
        # execute the function
        function_result = dao.get_all_reimbursements()

        # get a new mock connection
        make_mock_connection()
        # retrieve all the reimbursements from the database manually
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM reimbursements")
        query_result = cursor.fetchall()

        # make sure the two results are the same
        self.assertEqual(function_result, query_result)

    def test_get_pending_reviews(self):
        # get a new mock connection
        make_mock_connection()
        # execute the function
        function_result = dao.get_pending_reviews()

        # get a new mock connection
        make_mock_connection()
        # retrieve all the reimbursements from the database manually
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM reimbursements WHERE status = 'pending'")
        query_result = cursor.fetchall()

        # make sure the two results are the same
        self.assertEqual(function_result, query_result)

    def test_get_past_reimbursements(self):
        # get a new mock connection
        make_mock_connection()
        # execute the function
        function_result = dao.get_past_reimbursements()

        # get a new mock connection
        make_mock_connection()
        # retrieve all the reimbursements from the database manually
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM reimbursements WHERE status = 'approved'")
        query_result = cursor.fetchall()

        # make sure the two results are the same
        self.assertEqual(function_result, query_result)

    # test our get_reimbursement function
    def test_get_reimbursement(self):
        # determine the highest current id
        reimbursement_id = get_highest_id()

        # get a new mock connection
        make_mock_connection()
        # execute the function
        function_result = dao.get_reimbursement(reimbursement_id)

        # get a new mock connection
        make_mock_connection()
        # retrieve the reimbursement from the database manually
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM reimbursements WHERE reimbursement_id = {reimbursement_id}")
        query_result = cursor.fetchone()

        # make sure the two results are the same
        self.assertEqual(function_result, query_result)

    # test our update_reimbursement function
    def test_update_reimbursement(self):
        # make a new reimbursement
        make_mock_connection()
        dao.create_reimbursement(1, 0.00, 'reason', datetime.datetime(1997, 12, 6, 12, 0, 0))

        # get the id of the new reimbursement
        reimbursement_id = get_highest_id()

        # get a new mock connection
        make_mock_connection()
        # execute the function
        dao.update_reimbursement(reimbursement_id, 35.42, 'actual reason', datetime.datetime(1997, 12, 7, 12, 0, 0))

        # retrieve the reimbursement from the database
        make_mock_connection()
        reimbursement = dao.get_reimbursement(reimbursement_id)

        # make sure that all the values are correct
        self.assertEqual(reimbursement[0], reimbursement_id)
        self.assertEqual(reimbursement[1], 1)
        self.assertEqual(reimbursement[2], 35.42)
        self.assertEqual(reimbursement[3], 'actual reason')
        self.assertEqual(reimbursement[4], datetime.datetime(1997, 12, 7, 12, 0, 0))
        self.assertEqual(reimbursement[5], None)
        self.assertEqual(reimbursement[6], None)
        self.assertEqual(reimbursement[7], None)
        self.assertEqual(reimbursement[8], 'pending')

    def test_review_reimbursement(self):
        # make a new reimbursement
        make_mock_connection()
        dao.create_reimbursement(1, 0.00, 'reason', datetime.datetime(1997, 12, 6, 12, 0, 0))

        # get the id of the new reimbursement
        reimbursement_id = get_highest_id()

        # get a new mock connection
        make_mock_connection()
        # execute the function
        dao.review_reimbursement(reimbursement_id, 2, 'reimbursement approved', datetime.datetime(1997, 12, 7, 12, 0, 0), 'approved')

        # retrieve the reimbursement from the database
        make_mock_connection()
        reimbursement = dao.get_reimbursement(reimbursement_id)

        # make sure that all the values are correct
        self.assertEqual(reimbursement[0], reimbursement_id)
        self.assertEqual(reimbursement[1], 1)
        self.assertEqual(reimbursement[2], 0.00)
        self.assertEqual(reimbursement[3], 'reason')
        self.assertEqual(reimbursement[4], datetime.datetime(1997, 12, 6, 12, 0, 0))
        self.assertEqual(reimbursement[5], 2)
        self.assertEqual(reimbursement[6], 'reimbursement approved')
        self.assertEqual(reimbursement[7], datetime.datetime(1997, 12, 7, 12, 0, 0))
        self.assertEqual(reimbursement[8], 'approved')

    # test out delete_reimbursement function
    def test_delete_reimbursement(self):
        # make a new reimbursement
        make_mock_connection()
        dao.create_reimbursement(1, 0.00, 'reason', datetime.datetime(1997, 12, 6, 12, 0, 0))

        # get the id of the new reimbursement
        reimbursement_id = get_highest_id()

        # get a new mock connection
        make_mock_connection()
        # execute the function
        dao.delete_reimbursement(reimbursement_id)

        # try to retrieve the reimbursement from the database
        make_mock_connection()
        reimbursement = dao.get_reimbursement(reimbursement_id)

        # make sure the reimbursement isn't in the database
        self.assertIsNone(reimbursement)

    def test_get_biggest_single_spender(self):
        # get a new mock connection
        make_mock_connection()
        # execute the function
        function_result = dao.get_biggest_single_spender()

        # get a new mock connection
        make_mock_connection()
        # retrieve the data from the database manually
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        query = """SELECT user_first_name, user_last_name FROM users WHERE user_id =
                        (SELECT employee_id FROM reimbursements WHERE amount =
                        (SELECT MAX (amount) FROM reimbursements WHERE status = 'approved') LIMIT 1)"""
        cursor.execute(query)
        query_result = cursor.fetchone()

        # make sure the two results are the same
        self.assertEqual(function_result, query_result)

    def test_biggest_total_spender(self):
        # get a new mock connection
        make_mock_connection()
        # execute the function
        function_result = dao.get_biggest_total_spender()

        # get a new mock connection
        make_mock_connection()
        # retrieve the data from the database manually
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        query = """SELECT user_first_name, user_last_name FROM users WHERE user_id = (SELECT employee_id FROM 
                        (SELECT employee_id, SUM(amount) AS amount_sum FROM reimbursements WHERE status = 'approved' 
                        GROUP BY employee_id ORDER BY amount_sum DESC LIMIT 1) AS employee)"""
        cursor.execute(query)
        query_result = cursor.fetchone()

        # make sure the two results are the same
        self.assertEqual(function_result, query_result)

    def test_get_average_amount(self):
        # get a new mock connection
        make_mock_connection()
        # execute the function
        function_result = dao.get_average_amount()

        # get a new mock connection
        make_mock_connection()
        # retrieve the data from the database manually
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT AVG (amount::numeric) FROM reimbursements WHERE status = 'approved'")
        query_result = cursor.fetchval()

        # make sure the two results are the same
        self.assertEqual(function_result, query_result)

    def test_get_highest_amount(self):
        # get a new mock connection
        make_mock_connection()
        # execute the function
        function_result = dao.get_highest_amount()

        # get a new mock connection
        make_mock_connection()
        # retrieve the data from the database manually
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT MAX (amount) FROM reimbursements WHERE status = 'approved'")
        query_result = cursor.fetchval()

        # make sure the two results are the same
        self.assertEqual(function_result, query_result)
