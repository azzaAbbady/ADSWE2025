# features/steps/auth_steps.py
from behave import *
from django.contrib.auth import authenticate

@given('I am logged in as "{username}"')
def step_impl(context, username):
    context.client.login(username=username, password='admin')

@then('I should see login error')
def step_impl(context):
    assert 'Invalid credentials' in context.response.content.decode()