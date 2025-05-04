Feature: Department Views
  Scenario: View employees in Engineering department
    Given the following employees exist:
      | first_name | last_name | department_id |
      | Alice      | Smith     | 1             |
      | Bob        | Johnson   | 2             |
      | Carol      | Williams  | 1             |
    When I visit "/departments/1/employees/"
    Then I should see 2 employees
    And I should see "Alice Smith" in the results
    And I should see "Carol Williams" in the results
    But I should not see "Bob Johnson"
    And the response should contain department name "Engineering"