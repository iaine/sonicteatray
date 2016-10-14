from nose.tools import assert_false, assert_true

import alsaaudio
import wave

from audioplay import Audio

def test_play_state():
    player = Audio()
    assert_true(player.current_position == 0.0)

def testplay_state_runs():
    player = Audio()
    card = None

    f = wave.open('DragonBite.wav', 'rb')
    device = alsaaudio.PCM(card=card)

    play = player.play(device, f)
    assert_true()
