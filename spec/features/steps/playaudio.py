'''
   Steps for interaction
'''

from behave import *
import subprocess

@given("I press the {play} button")
def step_impl(context, play):
    pass
    #raise NotImplementedError("STEP: Given I press the " + play + "button")

@given('I am not playing audio')
def step_impl(context):
    pass

@when("I emit the signal {signal}")
def step_impl(context, signal):
    if signal is 25:
        print(signal)
        subprocess.check_call(["python", "../../../teatray/teatray.py "+ signal])
        assert TRUE

@when('I give the play section a file called {audio_file}')
def step_impl(context, audio_file):
    pass

@then('I can play the file')
def step_impl(context):
    pass

@then('I can get an error')
def step_impl(context):
    pass

@then("the audio signal {play_state}")
def step_impl(context, play_state):
    pass
