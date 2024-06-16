Feature: User Registration

  Scenario Outline: User Registration
    Given The user is on the registration page
    When User submits registration details with email:<email> and password:<password>
    Then User should receive a status code <status_code>
    And The response contains <expected_response>

    Examples:
      | email                | password  | status_code | expected_response |
      | eve.holt@reqres.in   | pistol    | 200         | success           |
      | duplicate@example.com| password1 | 400         | error             |
      | invalidemail         | password2 | 400         | error             |
      |                      | password3 | 400         | error             |
      | eve.holt@reqres.in   |           | 400         | error             |