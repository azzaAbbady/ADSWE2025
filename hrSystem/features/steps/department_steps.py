from behave import *
from django.urls import reverse
from datetime import datetime, timedelta
from hrSystem.models import Attendance, Employee, User

# --- Scenario: View My Attendance for the Last 30 Days ---

@given('I am logged in as employee "{email}"')
def step_impl(context, email):
    # Create test employee and log in
    context.employee = Employee.objects.create(
        name="John Doe",
        email=email,
        department=Department.objects.create(name="IT")
    )
    context.user = User.objects.create_user(
        username=email,
        password='test123'
    )
    context.client.login(username=email, password='test123')

    # Create sample attendance records
    for day in range(30):  # Last 30 days
        Attendance.objects.create(
            employee=context.employee,
            date=datetime.now() - timedelta(days=day),
            status="Present" if day % 5 != 0 else "Absent"  # Sample logic
        )

@when('I visit the attendance page')
def step_impl(context):
    context.attendance_url = reverse('view_attendance')
    context.response = context.client.get(context.attendance_url)

@then('I should see my attendance records for the last {days} days')
def step_impl(context, days):
    content = context.response.content.decode()
    assert "Present" in content
    assert "Absent" in content
    assert str(datetime.now().date()) in content  # Today's date should appear

# --- Scenario: Filter Attendance by Date Range ---

@when('I select date range from "{start_date}" to "{end_date}"')
def step_impl(context, start_date, end_date):
    context.filter_url = reverse('filter_attendance')  # Replace with your URL
    context.response = context.client.post(
        context.filter_url,
        {'start_date': start_date, 'end_date': end_date}
    )

@when('I click "Filter"')
def step_impl(context):
    pass  # Handled in the previous step (POST request)

@then('I should see only records between "{start_date}" and "{end_date}"')
def step_impl(context, start_date, end_date):
    content = context.response.content.decode()
    assert start_date in content
    assert end_date in content
    assert "2023-10-15" in content  # Example record in range
    assert "2023-11-01" not in content  # Should not appear