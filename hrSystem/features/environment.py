import os
import django
from behave.runner import Context

def before_all(context: Context):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'hrSystem.settings'
    django.setup()

def before_scenario(context, scenario):
    from django.core.management import call_command
    call_command('loaddata', 'test_data.json')
    from django.db import connection
    connection.creation.create_test_db()

def after_scenario(context, scenario):
    from django.db import connection
    connection.close()
    connection.creation.destroy_test_db()
