Feature: Employee Login  
  As an employee  
  I want to log in securely  
  So that I can access my HR dashboard  

  Scenario: Successful Login  
    Given I am on the login page  
    When I enter valid name "admin" and password "admin"  
    And I click the "Login" button  
    Then I should be redirected to the dashboard  

  Scenario: Failed Login (Invalid Credentials)  
    Given I am on the login page  
    When I enter invalid name "john@hr.com" and password "wrongpass"  
    And I click the "Login" button  
    Then I should see "Invalid email or password"  