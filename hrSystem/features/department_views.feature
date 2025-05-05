Feature: Department Views
  Scenario: View employees in "Sales" department
    Given the following employees exist:
      | first_name | last_name | department_id |
      | ayman      | ahmed     | 5             |
    When I visit "/departments/5/employees/"
    Then I should see 1 employees
    And I should see "ayman ahmed" in the results
    But I should not see "Bob Johnson"
    And the response should contain department name "Sales"