# import our flask app and query object to access it's functions from app.py
from src.app import app, request, session, redirect

# import our service level logic for users
import src.service.user_service as service

# import json formatting logic
from src.models.user import User, UserEncoder
from json import dumps

# set up logging
import logging
user_logger = logging.getLogger('user_logger')
user_logger.setLevel(logging.INFO)
log_handler = logging.FileHandler('logging/users.log')
user_logger.addHandler(log_handler)


@app.route('/users', methods=['POST'])
def create_user():
    # get data from request body
    user_json = request.get_json()
    user_first_name = user_json['user_first_name']
    user_last_name = user_json['user_last_name']
    user_email = user_json['user_email']
    user_password = user_json['user_password']
    is_manager = user_json['is_manager']

    # call service function to create new user
    result = service.create_user(user_first_name, user_last_name, user_email, user_password, is_manager)

    if isinstance(result, User):
        # log creation of new user
        user_logger.info(f"""Created new user with Name: {user_first_name} {user_last_name},
                      Email: {user_email}, Is manager? {is_manager}.""")

        # return success message
        return "User created successfully.", 201
    else:
        return result, 400


@app.route('/users/<int:user>', methods=['GET'])
def find_user(user):
    # get result from service function
    result = service.get_user(user)

    if isinstance(result, User):
        # return the result in json form
        return dumps(result, cls=UserEncoder), 200
    else:
        # return error message
        return result, 404


@app.route('/users', methods=['GET'])
def find_all_users():
    # get result from service function
    result = service.get_all_users()

    # return the result in json form
    return dumps(result, cls=UserEncoder), 200


@app.route('/users/login', methods=['POST'])
def login():
    # get data from request form
    email = request.form.get('email')
    password = request.form.get('password')

    # get result from service function
    result = service.user_login(email, password)
    if isinstance(result, int):
        # log the user in
        user = service.get_user(result)
        session['user_id'] = user.get_id()
        session['user_name'] = user.get_name()
        session['user_email'] = user.get_email()
        session['is_manager'] = user.is_manager()

        # redirect the user to the home page
        return redirect('../home.html')
    else:
        # return the user to the page they were on without logging them in
        return redirect(request.referrer)


@app.route('/users/logout', methods=['POST'])
def logout():
    # get rid of all the session variables
    session.clear()

    # the user wont see this but we have to return something
    return "success"


@app.route('/users/<int:user>', methods=['PUT'])
def update_user(user):
    # get data from request body
    user_json = request.get_json()
    user_first_name = user_json['user_first_name']
    user_last_name = user_json['user_last_name']
    user_email = user_json['user_email']
    is_manager = user_json['is_manager']

    # user service function to update the user
    result = service.update_user(user, user_first_name, user_last_name, user_email, is_manager)

    # log update of user
    user_logger.info(f"""Updated info for user with ID: {user}, Name: {user_first_name} {user_last_name},
                          Email: {user_email}, Is manager? {is_manager}.""")

    # return success or failure message message
    return result


@app.route('/users/<int:user>', methods=['DELETE'])
def delete_user(user):
    # use service function to delete the user
    result = service.delete_user(user)

    # log delete of user
    user_logger.info(f"Deleted user with ID: {user}")

    # return success or failure message message
    return result
