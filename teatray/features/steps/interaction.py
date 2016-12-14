from behave import *

from tilehandle import TileState

_tmp_state = None
asignal = None

@given(u'I am silent')
def step_impl(context):
    t = TileState()
    assert t.state is False

@when(u'I emit the signal {signal}')
def step_impl(context, signal):
    global _tmp_state, asignal
    t = TileState()
    asignal = t.handle_tile(int(signal))
    _tmp_state = t.state

@then(u'the audio signal starts')
def step_impl(context):
    global _tmp_state
    assert _tmp_state is True

@then(u'the audio for "wheatear.mp3" begins')
def step_impl(context):
    global _tmp_state, asignal
    assert _tmp_state is True
    assert asignal == "wheatear.mp3"