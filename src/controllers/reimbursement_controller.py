# import our flask app and database connection/cursor from app.py
import datetime

from src.app import app, request, session, redirect

# import our service level logic for reimbursements
import src.service.reimbursement_service as service

# import json formatting logic
from src.models.reimbursement import ReimbursementEncoder
from json import dumps

# set up logging
import logging
reimbursement_logger = logging.getLogger('reimbursement_logger')
reimbursement_logger.setLevel(logging.INFO)
log_handler = logging.FileHandler('logging/reimbursements.log')
reimbursement_logger.addHandler(log_handler)


@app.route('/reimbursements', methods=['POST'])
def create_reimbursement():
    employee_id = session.get('user_id')
    amount = request.form.get('amount')
    reason = request.form.get('reason')
    date = datetime.datetime.now().replace(microsecond=0)

    # call service function to create new reimbursement
    service.create_reimbursement(employee_id, amount, reason, date)

    # log creation of new reimbursement
    reimbursement_logger.info(f"""Created new reimbursement for user: {employee_id}, 
                                  Amount: {amount}, Reason: {reason}, 
                                  Created: {date}.""")

    # send the user to the reimbursements page
    return redirect('http://localhost:5000/reimbursements.html')


@app.route('/users/<int:user_id>/reimbursements', methods=['GET'])
def get_all_reimbursements(user_id):
    # use service layer logic to get results
    result = service.get_all_reimbursements(user_id)
    result = dumps(result, cls=ReimbursementEncoder)

    # return the result in json form
    return result, 200


@app.route('/users/<int:user_id>/reviews', methods=['GET'])
def get_all_reviews(user_id):
    # use service layer logic to get results
    result = service.get_all_reviews(user_id)
    result = dumps(result, cls=ReimbursementEncoder)

    # return the result in json form
    return result, 200


@app.route('/reviews/pending', methods=['GET'])
def get_pending_reviews():
    # use service layer logic to get results
    result = service.get_pending_reviews()
    result = dumps(result, cls=ReimbursementEncoder)

    # return the result in json form
    return result, 200


@app.route('/reimbursements/past', methods=['GET'])
def get_past_reimbursements():
    # use service layer logic to get results
    result = service.get_past_reimbursements()
    result = dumps(result, cls=ReimbursementEncoder)

    # return the result in json form
    return result, 200


@app.route('/reimbursements/<int:reimbursement_id>', methods=['GET'])
def get_reimbursement(reimbursement_id):
    # use service layer logic to get results
    result = service.get_reimbursement(reimbursement_id)
    result = dumps(result, cls=ReimbursementEncoder)

    # return the result in json form
    return result, 200


@app.route('/reimbursements/<int:reimbursement_id>', methods=['POST'])
def update_reimbursement(reimbursement_id):
    # get data from request form
    amount = request.form.get('amount')
    reason = request.form.get('reason')
    date = datetime.datetime.now().replace(microsecond=0)

    # use service layer logic to update the reimbursement
    service.update_reimbursement(reimbursement_id, amount, reason, date)

    # log update of reimbursement
    reimbursement_logger.info(f"""Updated reimbursement with ID: {reimbursement_id}, 
                                      Amount: {amount}, Reason: {reason}, 
                                      Updated: {date}.""")

    # return the user to the page they were just on
    return redirect(request.referrer)


@app.route('/reviews/<int:reimbursement_id>', methods=['POST'])
def review_reimbursement(reimbursement_id):
    # get manager id from session
    manager_id = session.get('user_id')
    # get data from request form
    review_comments = request.form.get('comments')
    status = request.form.get('result')
    date = datetime.datetime.now().replace(microsecond=0)

    # use service layer logic to update the reimbursement
    service.review_reimbursement(reimbursement_id, manager_id, review_comments, date, status)

    # log review of reimbursement
    reimbursement_logger.info(f"""Completed review for reimbursement with ID: {reimbursement_id}, 
                                          Comments: {review_comments}, Result: {status}, 
                                          Reviewed By:{manager_id}, On: {date}.""")

    # return the user to the page they were just on
    return redirect(request.referrer)


@app.route('/stats', methods=['GET'])
def get_stats():
    result = service.get_stats()

    return dumps(result)


@app.route('/reimbursements/<int:reimbursement_id>', methods=['DELETE'])
def delete_reimbursement(reimbursement_id):

    # use service layer logic to delete the review
    service.delete_reimbursement(reimbursement_id)

    # log delete of reimbursement
    reimbursement_logger.info(f"Deleted reimbursement with ID: {reimbursement_id}")

    # return success message
    return "Reimbursement deleted successfully.", 201






