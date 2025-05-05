from behave import *
from hr.models import Employee

@given('these employees exist')
def step_impl(context):
    for row in context.table:
        Employee.objects.create(
            name=row['first_name'],
            department=row['Department']
        )

@then('I should see only "{name}" in results')
def step_impl(context, name):
    assert name in context.response.content.decode()
    assert "Bob" not in context.response.content.decode()