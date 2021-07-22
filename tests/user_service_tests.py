# import unittest to handle our testing
import unittest

# unittest comes with built-in mocking functionality
from unittest.mock import Mock

# import User class and user_service module to be tested
from src.models.user import User
from src.service import user_service as service

# import our client dao so that we can create a mock
from src.dao import user_dao as dao


class UserServiceTests(unittest.TestCase):
    def setUp(self):
        # create a mock so that when functions are called, mock values (stubs) are returned instead of real data
        dao.create_user = Mock()
        dao.create_login = Mock()
        dao.check_email = Mock(return_value=None)
        dao.check_password= Mock('password')
        dao.get_all_users = Mock(return_value=[(1, 'Tony', 'James', 'TonyJames@email.com', False),
                                               (2, 'Alex', 'Smith', 'AlexSmith@email.com', True)])
        dao.get_user = Mock(return_value=(1, 'Adam', 'Smith', 'AdamSmith@email.com', False))
        dao.update_user = Mock()
        dao.delete_user = Mock()

    # test our create user function
    def test_create_user(self):
        # execute the function
        service.create_user('Tim', 'Smith', 'TimSmith@email.com', '', False)

        # assert that the dao create user function was called with the correct information
        dao.create_user.assert_called_with('Tim', 'Smith', 'TimSmith@email.com', False)
        # since we're hashing out password, we can't check for the call arguments but we'll
        #   make sure the create login function was called once
        self.assertEqual(dao.create_login.call_count, 1)

    # test our get all users function
    def test_get_all_users(self):
        # execute the function
        result = service.get_all_users()

        # assert the function returned a dictionary
        self.assertIsInstance(result, dict)

        # assert that every item in the dictionary is a User object
        for user in result.values():
            self.assertIsInstance(user, User)

        # assert that our returned users have the correct information
        self.assertEqual(result[1].get_id(), 1)
        self.assertEqual(result[1].get_name(), 'Tony James')
        self.assertEqual(result[1].get_email(), 'TonyJames@email.com')
        self.assertEqual(result[1].is_manager(), False)
        self.assertEqual(result[2].get_id(), 2)
        self.assertEqual(result[2].get_name(), 'Alex Smith')
        self.assertEqual(result[2].get_email(), 'AlexSmith@email.com')
        self.assertEqual(result[2].is_manager(), True)

    # test our get user function
    def test_get_user(self):
        # execute the function
        result = service.get_user(1)

        # assert the function returned a User object
        self.assertIsInstance(result, User)

        # assert that our returned user has the correct information
        self.assertEqual(result.get_id(), 1)
        self.assertEqual(result.get_name(), 'Adam Smith')
        self.assertEqual(result.get_email(), 'AdamSmith@email.com')
        self.assertEqual(result.is_manager(), False)

    # test our update user function
    def test_update_user(self):
        # execute the function
        service.update_user(1, 'Adam', 'Smith', 'AdamSmith@email.com', True)

        # assert that the dao update user function was called with the correct information
        dao.update_user.assert_called_with(1, 'Adam', 'Smith', 'AdamSmith@email.com', True)

    # test our delete user function
    def test_delete_user(self):
        # execute the function
        service.delete_user(2)

        # assert that the dao delete user function was called with the correct information
        dao.delete_user.assert_called_with(2)
