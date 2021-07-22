# import unittest to handle our testing
import unittest
from datetime import datetime

# unittest comes with built-in mocking functionality
from unittest.mock import Mock

# import Reimbursement class and reimbursement_service module to be tested
from src.models.reimbursement import Reimbursement
from src.service import reimbursement_service as service

# import our reimbursement dao so that we can create a mock
from src.dao import reimbursement_dao as dao


class ReimbursementServiceTests(unittest.TestCase):
    def setUp(self):
        # create a mock so that when functions are called, mock values (stubs) are returned instead of real data
        dao.create_reimbursement = Mock()
        dao.get_all_reimbursements = Mock(return_value=[(1, 1, 25.56, 'reason 1', datetime(1997, 12, 6, 12, 0, 0), 2,
                                                         'yes', datetime(1997, 12, 7, 12, 0, 0), 'approved'),
                                                        (2, 1, 120.76, 'reason 2', datetime(2021, 12, 6, 12, 0, 0),
                                                         None, None, None, 'pending')])
        dao.get_past_reimbursements = Mock(return_value=[(1, 1, 25.56, 'reason 1', datetime(1997, 12, 6, 12, 0, 0), 2,
                                                          'yes', datetime(1997, 12, 7, 12, 0, 0), 'approved'),
                                                         (2, 1, 120.76, 'reason 2', datetime(2021, 12, 6, 12, 0, 0), 2,
                                                          'no', datetime(1997, 12, 7, 12, 0, 0), 'denied')])
        dao.get_pending_reviews = Mock(return_value=[(1, 1, 25.56, 'reason 1', datetime(1997, 12, 6, 12, 0, 0), None,
                                                      None, None, 'pending'),
                                                     (2, 1, 120.76, 'reason 2', datetime(2021, 12, 6, 12, 0, 0),
                                                      None, None, None, 'pending')])
        dao.get_reimbursement = Mock(return_value=(3, 2, 98.99, 'reason 3', datetime(1997, 12, 6, 12, 0, 0), None,
                                                   None, None, 'pending'))
        dao.update_reimbursement = Mock()
        dao.review_reimbursement = Mock()
        dao.delete_reimbursement = Mock()
        dao.get_biggest_single_spender = Mock(return_value=('Joe', 'Miller'))
        dao.get_biggest_total_spender = Mock(return_value=('Marcus', 'Kee'))
        dao.get_average_amount = Mock(return_value=33.3333)
        dao.get_highest_amount = Mock(return_value=99999.99)

    # test our create reimbursement function
    def test_create_reimbursement(self):
        # execute the function
        service.create_reimbursement(1, 25.56, 'reason 1', datetime(1997, 12, 6, 12, 0, 0))

        # assert that the dao create reimbursement function was called with the correct information
        dao.create_reimbursement.assert_called_with(1, 25.56, 'reason 1', datetime(1997, 12, 6, 12, 0, 0), None, None,
                                                    None, 'pending')

    # test our get all reimbursements function
    def test_get_all_reimbursements(self):
        # execute the function
        result = service.get_all_reimbursements(1)

        # assert the function returned a dictionary
        self.assertIsInstance(result, dict)

        # assert that every item in the dictionary is a Reimbursement object
        for reimbursement in result.values():
            self.assertIsInstance(reimbursement, Reimbursement)

        # assert that our returned reimbursements have the correct information
        self.assertEqual(result[1].get_reimbursement_id(), 1)
        self.assertEqual(result[1].get_employee_id(), 1)
        self.assertEqual(result[1].get_amount(), '$25.56')
        self.assertEqual(result[1].get_reason(), 'reason 1')
        self.assertEqual(result[1].get_date_created(), '1997-12-06 12:00:00')
        self.assertEqual(result[1].get_manager_id(), 2)
        self.assertEqual(result[1].get_review_comments(), 'yes')
        self.assertEqual(result[1].get_date_reviewed(), '1997-12-07 12:00:00')
        self.assertEqual(result[1].get_status(), 'approved')
        self.assertEqual(result[2].get_reimbursement_id(), 2)
        self.assertEqual(result[2].get_employee_id(), 1)
        self.assertEqual(result[2].get_amount(), '$120.76')
        self.assertEqual(result[2].get_reason(), 'reason 2')
        self.assertEqual(result[2].get_date_created(), '2021-12-06 12:00:00')
        self.assertEqual(result[2].get_manager_id(), None)
        self.assertEqual(result[2].get_review_comments(), None)
        self.assertEqual(result[2].get_date_reviewed(), 'None')
        self.assertEqual(result[2].get_status(), 'pending')

    # test our get all reviews function
    def test_get_all_reviews(self):
        # execute the function
        result = service.get_all_reviews(1)

        # assert the function returned a dictionary
        self.assertIsInstance(result, dict)

        # assert that every item in the dictionary is a Reimbursement object
        for reimbursement in result.values():
            self.assertIsInstance(reimbursement, Reimbursement)

        # assert that our returned reimbursements have the correct information
        self.assertEqual(result[1].get_reimbursement_id(), 1)
        self.assertEqual(result[1].get_employee_id(), 1)
        self.assertEqual(result[1].get_amount(), '$25.56')
        self.assertEqual(result[1].get_reason(), 'reason 1')
        self.assertEqual(result[1].get_date_created(), '1997-12-06 12:00:00')
        self.assertEqual(result[1].get_manager_id(), 2)
        self.assertEqual(result[1].get_review_comments(), 'yes')
        self.assertEqual(result[1].get_date_reviewed(), '1997-12-07 12:00:00')
        self.assertEqual(result[1].get_status(), 'approved')
        self.assertEqual(result[2].get_reimbursement_id(), 2)
        self.assertEqual(result[2].get_employee_id(), 1)
        self.assertEqual(result[2].get_amount(), '$120.76')
        self.assertEqual(result[2].get_reason(), 'reason 2')
        self.assertEqual(result[2].get_date_created(), '2021-12-06 12:00:00')
        self.assertEqual(result[2].get_manager_id(), None)
        self.assertEqual(result[2].get_review_comments(), None)
        self.assertEqual(result[2].get_date_reviewed(), 'None')
        self.assertEqual(result[2].get_status(), 'pending')

    # test our get all past reimbursements function
    def test_get_past_reimbursements(self):
        # execute the function
        result = service.get_past_reimbursements()

        # assert the function returned a dictionary
        self.assertIsInstance(result, dict)

        # assert that every item in the dictionary is a Reimbursement object
        for reimbursement in result.values():
            self.assertIsInstance(reimbursement, Reimbursement)

        # assert that our returned reimbursements have the correct information
        self.assertEqual(result[1].get_reimbursement_id(), 1)
        self.assertEqual(result[1].get_employee_id(), 1)
        self.assertEqual(result[1].get_amount(), '$25.56')
        self.assertEqual(result[1].get_reason(), 'reason 1')
        self.assertEqual(result[1].get_date_created(), '1997-12-06 12:00:00')
        self.assertEqual(result[1].get_manager_id(), 2)
        self.assertEqual(result[1].get_review_comments(), 'yes')
        self.assertEqual(result[1].get_date_reviewed(), '1997-12-07 12:00:00')
        self.assertEqual(result[1].get_status(), 'approved')
        self.assertEqual(result[2].get_reimbursement_id(), 2)
        self.assertEqual(result[2].get_employee_id(), 1)
        self.assertEqual(result[2].get_amount(), '$120.76')
        self.assertEqual(result[2].get_reason(), 'reason 2')
        self.assertEqual(result[2].get_date_created(), '2021-12-06 12:00:00')
        self.assertEqual(result[2].get_manager_id(), 2)
        self.assertEqual(result[2].get_review_comments(), 'no')
        self.assertEqual(result[2].get_date_reviewed(), '1997-12-07 12:00:00')
        self.assertEqual(result[2].get_status(), 'denied')

    # test our get pending reviews function
    def test_get_pending_reviews(self):
        # execute the function
        result = service.get_pending_reviews()

        # assert the function returned a dictionary
        self.assertIsInstance(result, dict)

        # assert that every item in the dictionary is a Reimbursement object
        for reimbursement in result.values():
            self.assertIsInstance(reimbursement, Reimbursement)

        # assert that our returned reimbursements have the correct information
        self.assertEqual(result[1].get_reimbursement_id(), 1)
        self.assertEqual(result[1].get_employee_id(), 1)
        self.assertEqual(result[1].get_amount(), '$25.56')
        self.assertEqual(result[1].get_reason(), 'reason 1')
        self.assertEqual(result[1].get_date_created(), '1997-12-06 12:00:00')
        self.assertEqual(result[1].get_manager_id(), None)
        self.assertEqual(result[1].get_review_comments(), None)
        self.assertEqual(result[1].get_date_reviewed(), 'None')
        self.assertEqual(result[1].get_status(), 'pending')
        self.assertEqual(result[2].get_reimbursement_id(), 2)
        self.assertEqual(result[2].get_employee_id(), 1)
        self.assertEqual(result[2].get_amount(), '$120.76')
        self.assertEqual(result[2].get_reason(), 'reason 2')
        self.assertEqual(result[2].get_date_created(), '2021-12-06 12:00:00')
        self.assertEqual(result[2].get_manager_id(), None)
        self.assertEqual(result[2].get_review_comments(), None)
        self.assertEqual(result[2].get_date_reviewed(), 'None')
        self.assertEqual(result[2].get_status(), 'pending')

    # test our get reimbursement function
    def test_get_reimbursement(self):
        # execute the function
        result = service.get_reimbursement(3)

        # assert the function returned a Reimbursement object
        self.assertIsInstance(result, Reimbursement)

        # assert that our returned reimbursement has the correct information
        self.assertEqual(result.get_reimbursement_id(), 3)
        self.assertEqual(result.get_employee_id(), 2)
        self.assertEqual(result.get_amount(), '$98.99')
        self.assertEqual(result.get_reason(), 'reason 3')
        self.assertEqual(result.get_date_created(), '1997-12-06 12:00:00')
        self.assertEqual(result.get_manager_id(), None)
        self.assertEqual(result.get_review_comments(), None)
        self.assertEqual(result.get_date_reviewed(), 'None')
        self.assertEqual(result.get_status(), 'pending')

    # test our update reimbursement function
    def test_update_reimbursement(self):
        # execute the function
        service.update_reimbursement(1, 25.56, 'reason 1', datetime(1997, 12, 6, 12, 0, 0))

        # assert that the dao update reimbursement function was called with the correct information
        dao.update_reimbursement.assert_called_with(1, 25.56, 'reason 1', datetime(1997, 12, 6, 12, 0, 0))

    # test our review reimbursement function
    def test_review_reimbursement(self):
        # execute the function
        service.review_reimbursement(1, 2, 'no', datetime(1997, 12, 6, 12, 0, 0), 'denied')

        # assert that the dao update reimbursement function was called with the correct information
        dao.review_reimbursement.assert_called_with(1, 2, 'no', datetime(1997, 12, 6, 12, 0, 0), 'denied')

    # test our delete reimbursement function
    def test_delete_reimbursement(self):
        # execute the function
        service.delete_reimbursement(1)

        # assert that the dao delete reimbursement function was called with the correct information
        dao.delete_reimbursement.assert_called_with(1)

    # test our get stats function
    def test_get_stats(self):
        # execute the function
        result = service.get_stats()

        # make sure that the function return a dictionary
        self.assertIsInstance(result, dict)

        # make sure that the result contains the correct information
        self.assertEqual(result['Biggest_Spender_Total'], 'Marcus Kee')
        self.assertEqual(result['Biggest_Spender_Single'], 'Joe Miller')
        self.assertEqual(result['Highest_Amount'], '$99,999.99')
        self.assertEqual(result['Average_Amount'], '$33.33')
