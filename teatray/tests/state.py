from nose.tools import *

from teatray import audioplay

def test_audio_false():
    play = Audio()
    assert_false(play.instance)
