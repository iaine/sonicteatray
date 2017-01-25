from nose.tools import *
import os
from tilehandle import TileState
import sqlite3
import time

def setup_db_func():
    c = sqlite3.connect('teatraystore.db')
    d = c.cursor()
    d.executemany("INSERT INTO sounds VALUES (?,?)", [(25, "wheatear.mp3"), (26, "cuckoo.mp3")])

def teardown_db_func():
    os.remove('teatraystore.db')

def test_tile_init():
    t = TileState()
    assert_false(t.state)

def test_tile_state_change():
    t = TileState()
    rec = t.handle_tile(25)
    assert_true(t.state)

@with_setup(setup_db_func, teardown_db_func)
def test_tile_handle():
    t = TileState()
    time.sleep(1)
    rec = t.handle_tile(25)
    assert_true(rec == "wheatear.mp3")
    assert_false(rec == "cuckoo.mp3")

@raises(Exception)
def test_tile_empty_handle():
    t = TileState()
    rec = t.handle_tile()
