from behave import *

from tilehandle import TileState
from dao import DAO
_tmp_state = None
asignal = None

@given(u'I am silent')
def step_impl(context):
    t = TileState()
    assert t.state is False

@given(u'I am playing audio from {tile}')
def step_impl(context, tile):
    global _tmp_state, asignal
    t = TileState()
    asignal = t.handle_tile(int(tile))
    assert t.state is True
    assert asignal == "wheatear.mp3"

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

@then(u'the audio for "{recording}" begins')
def step_impl(context, recording):
    global _tmp_state, asignal
    assert _tmp_state is True
    assert asignal == recording

@then(u'the time {pin} stopped is recorded')
def step_impl(context, pin):
    raise NotImplementedError(u'STEP: Then the time 25 stopped is recorded')
