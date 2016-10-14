'''
   Steps for interaction
'''

from behave import *
import subprocess

import teatray

@given("I press the {play} button")
def step_impl(context, play):
    pass
    #raise NotImplementedError("STEP: Given I press the " + play + "button")

@when("I emit the signal {signal}")
def step_impl(context, signal):
    if signal is 25:
        print(signal)
        subprocess.check_call(["python", "teatray "+ signal])
        assert TRUE

@then("the audio signal {play_state}")
def step_impl(context, play_state):
    pass
