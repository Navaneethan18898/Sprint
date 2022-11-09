Feature: Flipkart Registration
  Scenario Outline: : Login data
    Given we navigate to the Flipkart url
    And close the login window
    When we hover over Login Button
    And Click on SignUp Link
    Then we validate the new user text
    And we type in the "<number>" field
    And Click on Continue button
    Then we type in "<password>" field
    And we click on the login button

    Examples:
      | number | password |
      | 9894366233 | Nava@18898 |
