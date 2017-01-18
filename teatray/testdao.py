from nose.tools import *
import os.path
import os

import sqlite3
from dao import DAO

def teardown_func():
    os.remove('*.db')

def test_dao_init():
    t = DAO()
    fname = os.path.isfile('teatraystore.db')
    assert_true(fname)

def test_dao_init_false():
    t = DAO()
    fname = os.path.isfile('store.db')
    assert_false(fname)

def test_dao_table_exists():
    t = DAO()
    conn = sqlite3.connect('teatraystore.db')
    db = conn.cursor()
    table = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('sounds',))
    assert_false(table.fetchone())
    t.check_table_exists('sounds')
    table_1 = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('sounds',))
    assert_true(table_1.fetchone())

def test_fetch_without_insert():
    t = DAO()
    assert_false(t.fetch(25) == "wheatear.mp3")

def test_insert_data():
    t = DAO()
    t.insert_data([(25, "wheatear.mp3"), (26, "cuckoo.mp3")])
    print t.fetch(25)

    assert_true(t.fetch(25) == "wheatear.mp3")
    assert_false(t.fetch(25) == "cuckoo.mp3")
