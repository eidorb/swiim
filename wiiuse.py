import ctypes
import logging
import os

logger = logging.getLogger('swiim.wiiuse')

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
        self._wiimotes = self.dll.wiiuse_init(1)

    def connect(self):
        found = self.dll.wiiuse_find(self._wiimotes, 1, 5)
        if found:
            return self.dll.wiiuse_connect(self._wiimotes, 1)

    def set_leds(self, led_state):
        self.dll.wiiuse_set_leds()