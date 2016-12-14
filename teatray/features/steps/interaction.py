from behave import *

@given(u'I am silent')
def step_impl(context):
    raise NotImplementedError(u'I am silent')

@when(u'I emit the signal {signal}')
def step_impl(context, signal):
    raise NotImplementedError(u'STEP: When I emit the signal 25')

@then(u'the audio signal starts')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the audio signal starts')
