import ctypes
from ctypes import Structure, c_void_p, c_int, c_byte, c_char, c_float
import logging
import os

logger = logging.getLogger('swiim.wiiuse')

class Event(object):
    WIIUSE_NONE = 0
    WIIUSE_EVENT = 1
    WIIUSE_STATUS = 2
    WIIUSE_CONNECT = 3
    WIIUSE_DISCONNECT = 4
    WIIUSE_UNEXPECTED_DISCONNECT = 5
    WIIUSE_READ_DATA = 6
    WIIUSE_NUNCHUK_INSERTED = 7
    WIIUSE_NUNCHUK_REMOVED = 8
    WIIUSE_CLASSIC_CTRL_INSERTED = 9
    WIIUSE_CLASSIC_CTRL_REMOVED = 10
    WIIUSE_GUITAR_HERO_3_CTRL_INSERTED = 11
    WIIUSE_GUITAR_HERO_3_CTRL_REMOVED = 12

class Wiimote(object):
    LED_NONE = 0x00
    LED_1 = 0x10
    LED_2 = 0x20
    LED_3 = 0x40
    LED_4 = 0x80
    BUTTON_TWO = 0x0001
    BUTTON_ONE = 0x0002
    BUTTON_B = 0x0004
    BUTTON_A = 0x0008
    BUTTON_MINUS = 0x0010
    BUTTON_ZACCEL_BIT6 = 0x0020
    BUTTON_ZACCEL_BIT7 = 0x0040
    BUTTON_HOME = 0x0080
    BUTTON_LEFT = 0x0100
    BUTTON_RIGHT = 0x0200
    BUTTON_DOWN = 0x0400
    BUTTON_UP = 0x0800
    BUTTON_PLUS = 0x1000
    BUTTON_ZACCEL_BIT4 = 0x2000
    BUTTON_ZACCEL_BIT5 = 0x4000
    BUTTON_UNKNOWN = 0x8000
    BUTTON_ALL = 0x1F9F

    def __init__(self):
        dll_dir = os.path.dirname(__file__)
        if os.name =='nt':
            dll_path = os.path.join(dll_dir, 'wiiuse.dll')
        else:
            dll_path = os.path.join(dll_dir, 'libwiiuse.so')
        logger.info('Using wiiuse library "%s"', dll_path)
        self.dll = ctypes.cdll.LoadLibrary(dll_path)
        # Initialise an array of wiimotes
        self._wiimotes = self.dll.wiiuse_init(1)
        self.disconnect = False

    def connect(self):
        """Attempt connection to a Wiimote, timeout after 5 seconds.
        Return the number of Wiimotes successfully connected to. In this case,
        it will 1 or 0."""

        found = self.dll.wiiuse_find(self._wiimotes, 1, 5)
        logger.debug('Found %s remote(s)', found)
        if found:
            connected = self.dll.wiiuse_connect(self._wiimotes, 1)
            logger.debug('Connected to %s remote(s)', connected)
            return connected

    def poll(self):
        logger.debug('Entering poll loop')
        while True:
            if not self.disconnect:
                event = self.dll.wiiuse_poll(self._wiimotes, 1)
                if event != Event.WIIUSE_NONE:
                    print 'some sort of event'
            else:
                logger.debug('Breaking from poll loop')
                break

    def set_leds(self, led_state):
        self.dll.wiiuse_set_leds()