import logging
from wiiuse.wiiuse import connect, find, init, poll

log = logging.getLogger('swiim.' + __name__)

TIMEOUT_SECONDS = 5

class WiimoteConnection(object):
    def __init__(self):
        self.wiimotes = init(1)
        self.wiimote = self.wiimotes.contents

    def connect(self):
        """Attempt a connection to a wiimote.

        Returns the number of wiimotes connected to if successful.

        """
        found = find(self.wiimotes, 1, TIMEOUT_SECONDS)
        if found:
            self.connected = connect(self.wiimotes, 1)
            if self.connected:
                log.info('Connected to a wiimote')
                return self.connected
        log.warning('Could not connect to any wiimotes')

    def poll(self):
        if poll(self.wiimotes, 1):
            device = self.wiimote.contents
            return device
