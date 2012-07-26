from wiiuse.wiiuse import find, init, poll

TIMEOUT_SECONDS = 5

class WiimoteConnection(object):
    def __init__(self):
        self.wiimotes = init(1)
        self.wiimote = self.wiimotes.contents

    def connect(self):
        return find(self.wiimotes, 1, TIMEOUT_SECONDS)

    def poll(self):
        if poll(self.wiimotes, 1):
            device = self.wiimote.contents
            return device
