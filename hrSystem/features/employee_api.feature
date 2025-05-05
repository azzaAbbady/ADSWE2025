@api
Feature: Employee API Operations
  Scenario: Add new employee via API
    Given the system has no employee with email "john.doe@example.com"
    When I send a POST request to "/api/employees/add/" with:
      """
      {
        "first_name": "test",
        "last_name": "BDD",
        "email": "john.doe@example.com",
        "department": 1,
        "position": "Developer",
        "salary": "80000.00",
        "hire_date": "2023-01-15"
      }
      """
    Then the response status code should be 201
    And the response should contain:
      """
      {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com"
      }
      """