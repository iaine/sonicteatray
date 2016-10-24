from behave import *
import subprocess

from teatray import audioplay

@given('I am not touching a tile')
def step_impl(context):
    pass

@given ('I am touching tile "{tile}"')
def step_impl(context, tile):
    pass

@when('I press tile "{tile}"')
def step_impl(context, tile):
    pass

@then('I can receive a response')
def step_impl(context):
    pass
