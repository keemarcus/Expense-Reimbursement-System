# import our reimbursement dao logic
import src.dao.reimbursement_dao as dao

# import our reimbursement logic
from src.models.reimbursement import Reimbursement


# we don't need any business logic for this function, so we simply call our dao function
def create_reimbursement(employee_id, amount, reason, date_created, manager_id=None, review_comments=None,
                         date_reviewed=None, status='pending'):
    dao.create_reimbursement(employee_id, amount, reason, date_created, manager_id, review_comments,
                             date_reviewed, status)


# call get all reimbursement function from dao layer and convert to usable data
def get_all_reimbursements(employee_id=None):
    # get results from dao
    db_reimbursement = dao.get_all_reimbursements(employee_id=employee_id)

    # set up a dictionary to hold our results
    results = {}

    # create a Reimbursement object for each entry in the database
    for row in db_reimbursement:
        reimbursement = Reimbursement(row[0], row[1], "${:,.2f}".format(row[2]), row[3], str(row[4]), row[5], row[6],
                                      str(row[7]), row[8])

        results[row[0]] = reimbursement

    # return the result
    return results


# call get all reimbursement function from dao layer and convert to usable data
def get_all_reviews(manager_id=None):
    # get results from dao
    db_reimbursement = dao.get_all_reimbursements(manager_id=manager_id)

    # set up a dictionary to hold our results
    results = {}

    # create a Reimbursement object for each entry in the database
    for row in db_reimbursement:
        reimbursement = Reimbursement(row[0], row[1], "${:,.2f}".format(row[2]), row[3], str(row[4]), row[5], row[6],
                                      str(row[7]), row[8])

        results[row[0]] = reimbursement

    # return the result
    return results


def get_past_reimbursements():
    # get results from dao
    db_reimbursement = dao.get_past_reimbursements()

    # set up a dictionary to hold our results
    results = {}

    # create a Reimbursement object for each entry in the database
    for row in db_reimbursement:
        reimbursement = Reimbursement(row[0], row[1], "${:,.2f}".format(row[2]), row[3], str(row[4]), row[5], row[6],
                                      str(row[7]), row[8])

        results[row[0]] = reimbursement

    # return the result
    return results


def get_pending_reviews():
    # get results from dao
    db_reimbursement = dao.get_pending_reviews()

    # set up a dictionary to hold our results
    results = {}

    # create a Reimbursement object for each entry in the database
    for row in db_reimbursement:
        reimbursement = Reimbursement(row[0], row[1], "${:,.2f}".format(row[2]), row[3], str(row[4]), row[5], row[6],
                                      str(row[7]), row[8])

        results[row[0]] = reimbursement

    # return the result
    return results


# call get reimbursement function from dao layer and convert it to usable data
def get_reimbursement(reimbursement_id):
    # get result from dao
    db_reimbursement = dao.get_reimbursement(reimbursement_id)

    # create a Reimbursement object for the result
    reimbursement = Reimbursement(
        db_reimbursement[0],
        db_reimbursement[1],
        "${:,.2f}".format(db_reimbursement[2]),
        db_reimbursement[3],
        str(db_reimbursement[4]),
        db_reimbursement[5],
        db_reimbursement[6],
        str(db_reimbursement[7]),
        db_reimbursement[8]
    )

    # return the result
    return reimbursement


# verify that the selected reimbursement exists then update it using our dao functions
def update_reimbursement(reimbursement_id, amount, reason, date_created):
    # use get reimbursement function to see if the id is associated with an existing reimbursement
    if dao.get_reimbursement(reimbursement_id) is None:
        return "404 Not Found: No such reimbursement exists with that ID", 404
    else:
        # use the update reimbursement function to make the desired changes in the database
        dao.update_reimbursement(reimbursement_id, amount, reason, date_created)

        # return success message
        return "Reimbursement updated successfully.", 201


def review_reimbursement(reimbursement_id, manager_id, review_comments, date_reviewed, status):
    # use get reimbursement function to see if the id is associated with an existing reimbursement
    if dao.get_reimbursement(reimbursement_id) is None:
        return "404 Not Found: No such reimbursement exists with that ID", 404
    else:
        # use the update reimbursement function to make the desired changes in the database
        dao.review_reimbursement(reimbursement_id, manager_id, review_comments, date_reviewed, status)

        # return success message
        return "Reimbursement reviewed successfully.", 201


# verify that the selected reimbursement exists in the database then delete it using our dao functions
def delete_reimbursement(reimbursement_id):
    # use get reimbursement function to see if the id is associated with an existing reimbursement
    if dao.get_reimbursement(reimbursement_id) is None:
        return "404 Not Found: No such reimbursement exists with that ID", 404
    else:
        # if reimbursement exists, then use delete reimbursement function to delete it from the database
        dao.delete_reimbursement(reimbursement_id)

        # use the get reimbursement function again to verify that the reimbursement was successfully deleted
        if dao.get_reimbursement(reimbursement_id) is None:
            return "Reimbursement successfully deleted", 205
        else:
            return "Unknown Error", 500


def get_stats():
    # run all our stat functions from the dao
    avg_amount = "${:,.2f}".format(dao.get_average_amount())
    highest_amount = "${:,.2f}".format(dao.get_highest_amount())
    row = dao.get_biggest_single_spender()
    biggest_single_spender = row[0] + ' ' + row[1]
    row = dao.get_biggest_total_spender()
    biggest_total_spender = row[0] + ' ' + row[1]
    results = dict(
        Biggest_Spender_Total=str(biggest_total_spender),
        Average_Amount=str(avg_amount),
        Highest_Amount=str(highest_amount),
        Biggest_Spender_Single=str(biggest_single_spender)
    )

    return results

