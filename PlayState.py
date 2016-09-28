from PlayerState import PlayerState

class PlayState(PlayerState):

    def play (self):
        print "play"

    def nextState(self):
        raise NotImplementedError
