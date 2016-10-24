from nose.tools import *
from teatray.tile import tile

def test_tile_init():
    t = Tile()
    assert_true(t)

def test_tile_handle():
    t = Tile()
    t.handle(25)
    assert_true("DragonBite.wav")
