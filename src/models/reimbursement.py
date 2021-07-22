# import JSONEncoder to set up our custom encoder
from json import JSONEncoder


class Reimbursement:
    # constructor
    def __init__(self, reimbursement_id, employee_id, amount, reason, date_created,
                 manager_id=None, review_comments=None, date_reviewed=None, status='pending'):
        self._reimbursement_id = reimbursement_id
        self._employee_id = employee_id
        self._amount = amount
        self._reason = reason
        self._date_created = date_created
        self._manager_id = manager_id
        self._review_comments = review_comments
        self._date_reviewed = date_reviewed
        self._status = status

    # getters
    def get_reimbursement_id(self):
        return self._reimbursement_id

    def get_employee_id(self):
        return self._employee_id

    def get_amount(self):
        return self._amount

    def get_reason(self):
        return self._reason

    def get_date_created(self):
        return self._date_created

    def get_manager_id(self):
        return self._manager_id

    def get_review_comments(self):
        return self._review_comments

    def get_date_reviewed(self):
        return self._date_reviewed

    def get_status(self):
        return self._status

    # setters
    def set_reimbursement_id(self, reimbursement_id):
        self._reimbursement_id = reimbursement_id

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    def set_amount(self, amount):
        self._amount = amount

    def set_reason(self, reason):
        self._reason = reason

    def set_date_created(self, reimbursement_date_created):
        self._date_created = reimbursement_date_created

    def set_manager_id(self, manager_id):
        self._manager_id = manager_id

    def set_review_comments(self, review_comments):
        self._review_comments = review_comments

    def set_date_reviewed(self, date_reviewed):
        self._date_reviewed = date_reviewed

    def set_status(self, status):
        self._status = status


# custom encoder
class ReimbursementEncoder(JSONEncoder):
    # override the default method
    def default(self, reimbursement):
        if isinstance(reimbursement, Reimbursement):
            return reimbursement.__dict__
        else:
            return super.default(self, reimbursement)
