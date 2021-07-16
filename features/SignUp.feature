Feature: To verify the SignUp functionality

  Scenario: Verify the Register Button
    Given open the login page
    When click on login button
    And click on register button
    Then I should see Customer Id field
    And I should see Proceed button
    And I should see back button
    And close browser