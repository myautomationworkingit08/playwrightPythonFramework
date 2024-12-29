Feature: Order Transaction
  Tests related to order transactions



  Scenario Outline: Verify order success massage is displayed in details page
    Given order is placed for an item by user with <username> and <password>
    And the user is on the landing page
    When user login to the portal with <username> and <password>
    And navigate to orders page
    And select the orderId
    Then order message is successfully displayed
    Examples:
      | username                 | password    |
      | automationuser@gmail.com | Superm@n001 |