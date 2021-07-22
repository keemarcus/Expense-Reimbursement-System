# here we will test the functionality available to all users
Feature: Employee Functionality

  # we must be signed in before performing each test
  Background:
    Given a user is logged in

  Scenario: A user would like to submit a new reimbursement request
    Given a user is on the home page
    When the user enters a valid amount and reason
    And the user pushes the submit button
    Then the user is redirected to their reimbursements page
    And a new reimbursement request was created

  Scenario: A user would like to submit a new reimbursement request
    Given a user is on the home page
    When the user enters a valid amount and reason
    And the user hits the enter button
    Then the user is redirected to their reimbursements page
    And a new reimbursement request was created

  Scenario: A user would like to submit a new reimbursement request
    Given a user is on their reimbursements page
    When the user enters a valid amount and reason
    And the user pushes the submit button
    Then the user is redirected to their reimbursements page
    And a new reimbursement request was created

  Scenario: A user would like to submit a new reimbursement request
    Given a user is on their reimbursements page
    When the user enters a valid amount and reason
    And the user hits the enter button
    Then the user is redirected to their reimbursements page
    And a new reimbursement request was created

  Scenario: A user would like to view their reimbursement requests
    Given a user is on their reimbursements page
    Then some reimbursements are displayed

  Scenario: A user would like to edit an existing reimbursement request
    Given a user is on their reimbursements page
    When the user pushes the edit button
    And the user enters a valid amount and reason
    And the user pushes the edit submit button
    Then the reimbursement information is updated

  Scenario: A user would like to edit an existing reimbursement request
    Given a user is on their reimbursements page
    When the user pushes the edit button
    And the user enters a valid amount and reason
    And the user hits the enter button
    Then the reimbursement information is updated