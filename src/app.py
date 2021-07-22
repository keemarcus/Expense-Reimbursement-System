# import flask
from flask import Flask, request, redirect, url_for, session, make_response, flash, render_template
# from flask_session import Session

# set up flask app
app = Flask(__name__, static_url_path='')


@app.route('/session/user_name', methods=['GET'])
def session_info_name():
    if session.get('user_name') is None:
        return "You are not signed in"
    else:
        return f"You are signed in as {session.get('user_name')}"


@app.route('/session/user_id', methods=['GET'])
def session_info_id():
    return str(session.get('user_id'))


@app.route('/session/is_manager', methods=['GET'])
def session_info_manager():
    return str(session.get('is_manager'))


# redirect to our static home page
@app.route('/', methods=['GET'])
def home():
    return redirect('../home.html')


# set up some basic error handlers
@app.errorhandler(404)
def handle_404(e):
    return "404 Not Found: No such resource exists on this server", 404


@app.errorhandler(500)
def handle_500(e):
    return "404 Not Found: No such resource exists on this server", 404
