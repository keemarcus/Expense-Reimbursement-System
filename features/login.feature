# here we will test our basic login functionality
Feature: Login

  Scenario: A user is on the home page and would like to login with correct credentials.
    Given a user is on the home page
    And a user enters the correct username and the correct password
    When the user pushes the submit button to login
    Then the user is logged in and redirected to the home page

  Scenario: A user is on the login page and would like to login with correct credentials.
    Given a user is on the login page
    And a user enters the correct username and the correct password
    When the user pushes the submit button
    Then the user is logged in and redirected to the home page

  Scenario: A user is on the home page and would like to login with correct credentials.
    Given a user is on the home page
    And a user enters the correct username and the correct password
    When the user hits the enter button to login
    Then the user is logged in and redirected to the home page

  Scenario: A user is on the login page and would like to login with correct credentials.
    Given a user is on the login page
    And a user enters the correct username and the correct password
    When the user hits the enter button
    Then the user is logged in and redirected to the home page
