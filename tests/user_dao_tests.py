# import testing and mock functionality
from unittest import mock, TestCase
# import our dao to test
from src.dao import user_dao as dao
# import database stuff
from utils import dbconfig
from pyodbc import connect


# we need to run this function to get a new mock connection everytime we need to access the test database
def make_mock_connection():
    mock_connection = connect("DRIVER=PostgreSQL UNICODE(x64);SERVER=localhost;PORT=5432;DATABASE=postgres;UID=postgres;PWD=password;Trusted_Connection=no;BoolsAsChar=0")
    dbconfig.get_connection = mock.Mock(return_value=mock_connection)


# this function is used to find the id of the most recent user in the database
def get_highest_id():
    # get a new mock connection
    make_mock_connection()
    # determine the largest id in the database
    connection = dbconfig.get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT MAX (user_id) FROM users")
    result = cursor.fetchone()
    if result[0] is None:
        return 0
    else:
        return result[0]


class UserDaoTests(TestCase):
    # test our create user function
    def test_create_user(self):
        # determine the highest current id
        user_id = get_highest_id()

        # get a new mock connection
        make_mock_connection()
        # execute the function
        dao.create_user('John', 'Adams', f"johnadams{user_id + 1}@email.com", False)

        # retrieve the new user from the database
        make_mock_connection()
        user = dao.get_user(user_id + 1)

        # make sure that all the values are correct
        self.assertEqual(user[0], user_id + 1)
        self.assertEqual(user[1], 'John')
        self.assertEqual(user[2], 'Adams')
        self.assertEqual(user[3], f"johnadams{user_id + 1}@email.com")
        self.assertEqual(user[4], False)

    def test_create_login(self):
        # determine the highest current id
        user_id = get_highest_id()

        # get a new mock connection
        make_mock_connection()
        # create a new user
        dao.create_user('John', 'Adams', f"johnadams{user_id + 1}@email.com", False)

        # get a new mock connection
        make_mock_connection()
        # execute the function
        dao.create_login(user_id, f"johnadams{user_id + 1}@email.com", "password")

        # check for the new user login in the database
        make_mock_connection()
        password = dao.check_password(f"johnadams{user_id + 1}@email.com")

        # make sure it returned the correct value
        self.assertEqual(password, "password")
    # test our get_all_users function
    def test_get_all_users(self):
        # get a new mock connection
        make_mock_connection()
        # execute the function
        function_result = dao.get_all_users()

        # get a new mock connection
        make_mock_connection()
        # retrieve all the users from the database manually
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        query_result = cursor.fetchall()

        # make sure the two results are the same
        self.assertEqual(function_result, query_result)

    # test our get_user function
    def test_get_user(self):
        # determine the highest current id
        user_id = get_highest_id()

        # get a new mock connection
        make_mock_connection()
        # execute the function
        function_result = dao.get_user(user_id)

        # get a new mock connection
        make_mock_connection()
        # retrieve the user from the database manually
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM users WHERE user_id = {user_id}")
        query_result = cursor.fetchone()

        # make sure the two results are the same
        self.assertEqual(function_result, query_result)

    # test our update_user function
    def test_update_user(self):
        # make a new user
        make_mock_connection()
        dao.create_user('New', 'User', 'newuser@email.com', False)

        # get the id of the new user
        user_id = get_highest_id()

        # get a new mock connection
        make_mock_connection()
        # execute the function
        dao.update_user(user_id, 'Jack', 'Miller', f"JMiller{user_id}@email.com", True)

        # retrieve the user from the database
        make_mock_connection()
        user = dao.get_user(user_id)

        # make sure that all the values are correct
        self.assertEqual(user[0], user_id)
        self.assertEqual(user[1], 'Jack')
        self.assertEqual(user[2], 'Miller')
        self.assertEqual(user[3], f"JMiller{user_id}@email.com")
        self.assertEqual(user[4], True)

    # test out delete_user function
    def test_delete_user(self):
        # make a new user
        make_mock_connection()
        dao.create_user('New', 'User', 'newuser@email.com', False)

        # get the id of the new user
        user_id = get_highest_id()

        # get a new mock connection
        make_mock_connection()
        # execute the function
        dao.delete_user(user_id)

        # try to retrieve the user from the database
        make_mock_connection()
        user = dao.get_user(user_id)

        # make sure the user isn't in the database
        self.assertIsNone(user)

    def test_check_email(self):
        # get a new mock connection
        make_mock_connection()
        # execute the function
        function_result = dao.check_email('JMiller3@email.com')

        # get a new mock connection
        make_mock_connection()
        # retrieve the data from the database manually
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT user_id FROM users WHERE user_email = 'JMiller3@email.com'")
        query_result = cursor.fetchval()

        # make sure the two results are the same
        self.assertEqual(function_result, query_result)

    def test_check_password(self):
        # get a new mock connection
        make_mock_connection()
        # execute the function
        function_result = dao.check_password('JMiller3@email.com')

        # get a new mock connection
        make_mock_connection()
        # retrieve the data from the database manually
        connection = dbconfig.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT user_password FROM user_logins WHERE user_email = 'JMiller3@email.com'")
        query_result = cursor.fetchval()

        # make sure the two results are the same
        self.assertEqual(function_result, query_result)
