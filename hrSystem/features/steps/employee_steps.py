from behave import *
from django.urls import reverse
from hr.models import Employee
import json

@given('the system has no employee with email "{email}"')
def step_impl(context, email):
    Employee.objects.filter(email=email).delete()

@when('I send a POST request to "{url}" with')
def step_impl(context, url):
    context.response = context.client.post(
        url,
        data=context.text,
        content_type='application/json'
    )

@then('the response status code should be {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code

@then('the response should contain')
def step_impl(context):
    expected = json.loads(context.text)
    actual = context.response.json()
    for key in expected:
        assert actual[key] == expected[key]