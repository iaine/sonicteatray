from nose.tools import assert_false, assert_true

from teatray import Audio

def test_play_state():
    player = Audio()
    assert_true(player.current_position == 0.0)

def testplay_state_runs():
    player = Audio()
    play = player.play("DragonBite.wav")
    assert_true()
