'''
   Main interface to be developed against
'''

import alsaaudio
import sys
import wave

from teatray.audioplay import Audio


signal = sys.argv[1]

if signal is None:
    print "No signal received"
    sys.exit()

player = Audio()
card = None


if signal == "25":
    f = wave.open('DragonBite.wav', 'rb')
    device = alsaaudio.PCM(card=card)

    player.play(device, f)
