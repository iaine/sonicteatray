'''
   Steps for interaction
'''

from behave import *

@given('I press the "{play}" button')
def step_impl(context, play):
    raise NotImplementedError(u'STEP: Given I press the play button')

@when('I emit the signal "{signal}"')
def step_impl(context, signal):
    raise NotImplementedError(u'STEP: When I emit the signal 25')

@then(' the audio signal "{play_state}"')
def step_impl(context, play_state):
    raise NotImplementedError(u'STEP: Then I get an audio signal')
