from nose.tools import *
from tilehandle import TileState

def test_tile_init():
    t = TileState()
    assert_false(t.state)

def test_tile_state_change():
    t = TileState()
    rec = t.handle_tile(25)
    assert_true(t.state)

def test_tile_handle():
    t = TileState()
    rec = t.handle_tile(25)
    assert rec == "wheatear.mp3"

def test_tile_handle_false():
    t = TileState()
    rec = t.handle_tile(25)
    assert rec != "cuckoo.mp3"

