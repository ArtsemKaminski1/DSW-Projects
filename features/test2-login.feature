Feature: User Login

  Scenario Outline: User login
    Given The user is on the login page
    When User submits login credentials with email:<email> and password:<password>
    Then User should receive a status code <status_code>
    And The response contains <expected_response>

    Examples:
      | email                | password  | status_code | expected_response         |
      | eve.holt@reqres.in   | pistol    | 200         | token                     |
      | eve.holt@reqres.in   | wrongpass | 400         | invalid_credentials_error |
      | nonexist@reqres.in   | pistol    | 400         | user_not_found_error      |
      |                      | pistol    | 400         | missing_email_error       |
      | eve.holt@reqres.in   |           | 400         | missing_password_error    |
