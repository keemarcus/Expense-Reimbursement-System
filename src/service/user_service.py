# import our user dao logic
import src.dao.user_dao as dao

# import our user logic
from src.models.user import User

# import our password hashing logic
from passlib.hash import sha256_crypt as p_hash


# we don't need any business logic for this function, so we simply call our dao function
def create_user(user_first_name, user_last_name, user_email, user_password, user_manager_privilege):
    # verify that the email isn't already assigned in the database
    if dao.check_email(user_email) is not None:
        return "Error: that email is associated with an existing user."
    else:
        # add the user info to the database
        dao.create_user(user_first_name, user_last_name, user_email, user_manager_privilege)

        # retrieve the id of the user we just created
        user_id = dao.check_email(user_email)

        # hash the password that the user gave us
        password = p_hash.hash(user_password)

        # add the login info to the database
        dao.create_login(user_id, user_email, password)

        # return the user we just created
        return get_user(user_id)


def user_login(user_email, user_password):
    # check for user email in the database
    if dao.check_email(user_email) is None:
        # if the email was invalid, return an error message
        return "Error: Invalid Login Info"
    else:
        # verify login information
        if p_hash.verify(user_password, dao.check_password(user_email)):
            # if the information was valid, return the id of the associated user
            return dao.check_email(user_email)
        else:
            # if the password was invalid, return an error message
            return "Error: Invalid Login Info"


# call get all users function from dao layer and convert to usable data
def get_all_users():
    # get results from dao
    db_users = dao.get_all_users()

    # set up a dictionary to hold our results
    results = {}

    # create a User object for each entry in the database
    for row in db_users:
        results[row[0]] = User(row[0], row[1], row[2], row[3], row[4])

    # return the result
    return results


# call get user function from dao layer and convert it to usable data
def get_user(user_id):
    # get result from dao
    db_user = dao.get_user(user_id)

    if db_user is None:
        # return error message
        return "404 Not Found: No such user exists with that ID."
    else:
        # create a User object for the result
        user = User(db_user[0], db_user[1], db_user[2], db_user[3], db_user[4])

        # return the result
        return user


# verify that the selected user exists then update it using our dao functions
def update_user(user_id, user_first_name, user_last_name, user_email, user_manager_privilege):
    # use get user function to see if the id is associated with an existing user
    if dao.get_user(user_id) is None:
        return "404 Not Found: No such user exists with that ID", 404
    else:
        # use the update user function to make the desired changes in the database
        dao.update_user(user_id, user_first_name, user_last_name, user_email, user_manager_privilege)

        # return success message
        return "User updated successfully.", 201


# verify that the selected user exists in the database then delete it using our dao functions
def delete_user(user_id):
    # use get user function to see if the id is associated with an existing user
    if dao.get_user(user_id) is None:
        return "404 Not Found: No such user exists with that ID", 404
    else:
        # if user exists, then use delete user function to delete it from the database
        dao.delete_user(user_id)

        # use the get user function again to verify that the user was successfully deleted
        if dao.get_user(user_id) is None:
            return "User successfully deleted", 205
        else:
            return "Unknown Error", 500
