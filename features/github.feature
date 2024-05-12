Feature: Github API Validation

  Scenario: Session management check
    Given I have github auth credentials
    When I Hit gitRepo API of github
    Then status code of response should be 200

#Feature: Accessing GitHub API with Authentication
#
#  Scenario: Get User Information
#    Given I am authenticated to GitHub
#    When I get user information
#    Then the response status code should be 200
#    And the response body should contain the user's data

#  Scenario: List User Repositories
#    Given I am authenticated to GitHub
#    When I list user repositories
#    Then the response status code should be 200
#    And the response body should contain a list of repositories