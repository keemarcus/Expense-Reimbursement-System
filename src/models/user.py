# import JSONEncoder to set up our custom encoder
from json import JSONEncoder


class User:
    # constructor
    def __init__(self, user_id, user_first_name, user_last_name, user_email, user_manager=False):
        self._user_id = user_id
        self._user_first_name = user_first_name
        self._user_last_name = user_last_name
        self._user_email = user_email
        self._user_manager = user_manager

    # custom to string method
    # def __str__(self):
    #     if self._user_manager:
    #         return f"""User ID: {self._user_id} User Name: {self._user_first_name} {self._user_last_name}
    #                 User Email: {self._user_email} User Level: Employee"""
    #     else:
    #         return f"""User ID: {self._user_id} User Name: {self._user_first_name} {self._user_last_name}
    #                 User Email: {self._user_email} User Level: Manager"""

    # getters
    def get_id(self):
        return self._user_id

    def get_name(self):
        return f"{self._user_first_name} {self._user_last_name}"

    def get_email(self):
        return self._user_email

    def is_manager(self):
        return self._user_manager

    # setters
    def set_id(self, user_id):
        self._user_id = user_id

    def set_name(self, user_first_name, user_last_name):
        self._user_first_name = user_first_name
        self._user_last_name = user_last_name

    def set_email(self, user_email):
        self._user_email = user_email

    def set_manager(self, user_manager):
        self._user_manager = user_manager


# custom encoder
class UserEncoder(JSONEncoder):
    # override the default method
    def default(self, user):
        if isinstance(user, User):
            return user.__dict__
        else:
            return super.default(self, user)
