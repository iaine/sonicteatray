'''
   Steps for interaction
'''

from behave import *
from teatray import Audio

@given('I press the "{play}" button')
def step_impl(context, play):
    raise NotImplementedError(u'STEP: Given I press the play button')

@when('I emit the signal "{signal}"')
def step_impl(context, signal):
    audio = Audio()
    if signal == 25:
        audio.play("DragonBite.wav")
        assert TRUE
    elif signal == 26:
        audio.play("DragonBite.wav")
        audio.pause()
        assert TRUE

@then(' the audio signal "{play_state}"')
def step_impl(context, play_state):
    raise NotImplementedError(u'STEP: Then I get an audio signal')
