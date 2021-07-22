# here we will test the functionality that is reserved for managers
Feature: Manager Functionality

  # we must be signed in as a manager before performing each test
  Background:
    Given a user is logged in as a manager

  Scenario: A manager would like to view all pending reimbursement requests
    Given a manager is on the pending reviews page
    Then some reimbursements are displayed

  Scenario: A manager would like to review a pending reimbursement request
    Given a manager is on the pending reviews page
    When the manager enters a valid comment and result
    And the user pushes the submit button
    Then the reimbursement request is no longer pending

  Scenario: A manager would like to review a pending reimbursement request
    Given a manager is on the pending reviews page
    When the manager enters a valid comment and result
    And the user hits the enter button
    Then the reimbursement request is no longer pending

  Scenario: A manager would like to view all their past reviews
    Given a manager is on their reviews page
    Then some review results are displayed

  Scenario: A manager would like to edit one of their past reviews
    Given a manager is on their reviews page
    When the user pushes the edit button
    And the manager enters a valid comment and result
    And the user pushes the submit button
    Then the reimbursement request is updated

  Scenario: A manager would like to edit one of their past reviews
    Given a manager is on their reviews page
    When the user pushes the edit button
    And the manager enters a valid comment and result
    And the user hits the enter button
    Then the reimbursement request is updated
#
  Scenario: A manager would like to view all past reimbursements
    Given a manager is on the past reimbursements page
    Then all past reimbursements are displayed

  Scenario: A manager would like to view the available reimbursement statistics
    Given a manager is on the statistics page
    Then the statistics are displayed