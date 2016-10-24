import alsaaudio

#from time import time


class Audio():
    def __init__(self):

        #paused state
        self.is_paused = False
        #the position of the track
        self.current_position = 0.0
        self.current_time  = 0

    def play(self, device, filename):
        '''
           Start to play a file
        '''
        # Set attributes
        device.setchannels(filename.getnchannels())
        device.setrate(filename.getframerate())

        # 8bit is unsigned in wav files
        if filename.getsampwidth() == 1:
            device.setformat(alsaaudio.PCM_FORMAT_U8)
        # Otherwise we assume signed data, little endian
        elif filename.getsampwidth() == 2:
            device.setformat(alsaaudio.PCM_FORMAT_S16_LE)
        elif filename.getsampwidth() == 3:
            device.setformat(alsaaudio.PCM_FORMAT_S24_LE)
        elif filename.getsampwidth() == 4:
            device.setformat(alsaaudio.PCM_FORMAT_S32_LE)
        else:
            raise ValueError('Unsupported format')

        device.setperiodsize(320)

        data = filename.readframes(320)
        while data:
            # Read data from stdin
            device.write(data)
            data = filename.readframes(320)
    


    def stop(self):
        '''
           Stop the audio
        '''
        raise NotImplementedError

    def pause(self):
        '''
           Pause the file as we've moved away
        '''
        # Alsaaudio suggests PCM.pause - so device.pause()
        raise NotImplementedError
