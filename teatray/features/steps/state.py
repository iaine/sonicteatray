from behave import *
import subprocess

from teatray import audioplay

@given('I am not playing anything')
def step_impl(context):
    pass

@given('I am playing "{audio_file}"')
def step_impl(context, audio_file):
    pass

@when('I  set up play')
def step_impl(context):
    pass

@when('I ask for "{audio_file}"')
def step_impl(context, audio_file):
    pass

@then('my state is {_state}')
def step_impl(context, _state):
    play = Audio()
    eq_(play.instance, _state)
