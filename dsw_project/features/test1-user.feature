Feature: Users

  Scenario Outline: Create a new user
    Given I am in super APP
    When User is created with name:<name> job:<job>
    Then Created user exist in the system
    And User name is <name>
    And User job is <job>

    Examples:
      | name     | job       |
      | Kaminski | Developer |
