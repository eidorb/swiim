import logging
import os
import ctypes
from ctypes import (c_char_p, c_int, c_ubyte, c_uint, c_uint16, c_float,
                    c_short, c_void_p, c_char, c_ushort,
                    CFUNCTYPE, Structure, POINTER, Union)
import sys
import time

log = logging.getLogger('swiim.wiiuse')

# Led bit masks
WIIMOTE_LED_NONE = 0x00
WIIMOTE_LED_1 = 0x10
WIIMOTE_LED_2 = 0x20
WIIMOTE_LED_3 = 0x40
WIIMOTE_LED_4 = 0x80
leds = {
    'WIIMOTE_LED_1': WIIMOTE_LED_1,
    'WIIMOTE_LED_2': WIIMOTE_LED_2,
    'WIIMOTE_LED_3': WIIMOTE_LED_3,
    'WIIMOTE_LED_4': WIIMOTE_LED_4,
}

# Button codes
WIIMOTE_BUTTON_TWO = 0x0001
WIIMOTE_BUTTON_ONE = 0x0002
WIIMOTE_BUTTON_B = 0x0004
WIIMOTE_BUTTON_A = 0x0008
WIIMOTE_BUTTON_MINUS = 0x0010
WIIMOTE_BUTTON_ZACCEL_BIT6 = 0x0020
WIIMOTE_BUTTON_ZACCEL_BIT7 = 0x0040
WIIMOTE_BUTTON_HOME = 0x0080
WIIMOTE_BUTTON_LEFT = 0x0100
WIIMOTE_BUTTON_RIGHT = 0x0200
WIIMOTE_BUTTON_DOWN = 0x0400
WIIMOTE_BUTTON_UP = 0x0800
WIIMOTE_BUTTON_PLUS = 0x1000
WIIMOTE_BUTTON_ZACCEL_BIT4 = 0x2000
WIIMOTE_BUTTON_ZACCEL_BIT5 = 0x4000
WIIMOTE_BUTTON_UNKNOWN = 0x8000
WIIMOTE_BUTTON_ALL = 0x1F9F
buttons = {
    'WIIMOTE_BUTTON_TWO': WIIMOTE_BUTTON_TWO,
    'WIIMOTE_BUTTON_ONE': WIIMOTE_BUTTON_ONE,
    'WIIMOTE_BUTTON_B': WIIMOTE_BUTTON_B,
    'WIIMOTE_BUTTON_A': WIIMOTE_BUTTON_A,
    'WIIMOTE_BUTTON_MINUS': WIIMOTE_BUTTON_MINUS,
    'WIIMOTE_BUTTON_HOME': WIIMOTE_BUTTON_HOME,
    'WIIMOTE_BUTTON_LEFT': WIIMOTE_BUTTON_LEFT,
    'WIIMOTE_BUTTON_RIGHT': WIIMOTE_BUTTON_RIGHT,
    'WIIMOTE_BUTTON_DOWN': WIIMOTE_BUTTON_DOWN,
    'WIIMOTE_BUTTON_UP': WIIMOTE_BUTTON_UP,
    'WIIMOTE_BUTTON_PLUS': WIIMOTE_BUTTON_PLUS,
}

# Nunchuk button codes
NUNCHUK_BUTTON_Z = 0x01
NUNCHUK_BUTTON_C = 0x02
NUNCHUK_BUTTON_ALL = 0x03

# Classic controller button codes
CLASSIC_CTRL_BUTTON_UP = 0x0001
CLASSIC_CTRL_BUTTON_LEFT = 0x0002
CLASSIC_CTRL_BUTTON_ZR = 0x0004
CLASSIC_CTRL_BUTTON_X = 0x0008
CLASSIC_CTRL_BUTTON_A = 0x0010
CLASSIC_CTRL_BUTTON_Y = 0x0020
CLASSIC_CTRL_BUTTON_B = 0x0040
CLASSIC_CTRL_BUTTON_ZL = 0x0080
CLASSIC_CTRL_BUTTON_FULL_R = 0x0200
CLASSIC_CTRL_BUTTON_PLUS = 0x0400
CLASSIC_CTRL_BUTTON_HOME = 0x0800
CLASSIC_CTRL_BUTTON_MINUS = 0x1000
CLASSIC_CTRL_BUTTON_FULL_L = 0x2000
CLASSIC_CTRL_BUTTON_DOWN = 0x4000
CLASSIC_CTRL_BUTTON_RIGHT = 0x8000
CLASSIC_CTRL_BUTTON_ALL = 0xFEFF

# Guitar Hero 3 button codes
GUITAR_HERO_3_BUTTON_STRUM_UP = 0x0001
GUITAR_HERO_3_BUTTON_YELLOW = 0x0008
GUITAR_HERO_3_BUTTON_GREEN = 0x0010
GUITAR_HERO_3_BUTTON_BLUE = 0x0020
GUITAR_HERO_3_BUTTON_RED = 0x0040
GUITAR_HERO_3_BUTTON_ORANGE = 0x0080
GUITAR_HERO_3_BUTTON_PLUS = 0x0400
GUITAR_HERO_3_BUTTON_MINUS = 0x1000
GUITAR_HERO_3_BUTTON_STRUM_DOWN = 0x4000
GUITAR_HERO_3_BUTTON_ALL = 0xFEFF

# Wiimote option flags
WIIUSE_SMOOTHING = 0x01
WIIUSE_CONTINUOUS = 0x02
WIIUSE_ORIENT_THRESH = 0x04
WIIUSE_INIT_FLAGS = (WIIUSE_SMOOTHING | WIIUSE_ORIENT_THRESH)

# Expansion codes
EXP_NONE = 0
EXP_NUNCHUK = 1
EXP_CLASSIC = 2
EXP_GUITAR_HERO_3 = 3

# Largest payload is 21 bytes. Add 2 for prefix and round up to power of 2
MAX_PAYLOAD = 32

# Wiiuse events
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

# Wiiuse data structures
class vec2b(Structure):
    _fields_ = [('x', c_ubyte),
                ('y', c_ubyte)]

class vec3b(Structure):
    _fields_ = [('x', c_ubyte),
                ('y', c_ubyte),
                ('z', c_ubyte)]

class vec3f(Structure):
    _fields_ = [('x', c_float),
                ('y', c_float),
                ('z', c_float)]

class orient(Structure):
    _fields_ = [('roll', c_float),
                ('pitch', c_float),
                ('yaw', c_float),
                ('a_roll', c_float),
                ('a_pitch', c_float)]

class gforce(Structure):
    _fields_ = [('x', c_float),
                ('y', c_float),
                ('z', c_float)]


class accel(Structure):
    _fields_ = [('cal_zero', vec3b),
                ('cal_g', vec3b),
                ('st_roll', c_float),
                ('st_pitch', c_float),
                ('st_alpha', c_float)]

class ir_dot(Structure):
    _fields_ = [('visible', c_ubyte),
                ('x', c_uint),
                ('y', c_uint),
                ('rx', c_short),
                ('ry', c_short),
                ('order', c_ubyte),
                ('size', c_ubyte)]

class ir(Structure):
    _fields_ = [('dot', ir_dot*4),
                ('num_dots', c_ubyte),
                ('aspect', c_int),
                ('pos', c_int),
                ('vres', c_uint*2),
                ('offset', c_int*2),
                ('state', c_int),
                ('ax', c_int),
                ('ay', c_int),
                ('x', c_int),
                ('y', c_int),
                ('distance', c_float),
                ('z', c_float)]

class joystick(Structure):
    _fields_ = [('max', vec2b),
                ('min', vec2b),
                ('center', vec2b),
                ('ang', c_float),
                ('mag', c_float)]

class nunchuk(Structure):
    _fields_ = [('accel_calib', accel),
                ('js', joystick),
                ('flags', POINTER(c_int)),
                ('btns', c_ubyte),
                ('btns_held', c_ubyte),
                ('btns_released', c_ubyte),
                ('orient_threshold', c_float),
                ('accel_threshold', c_int),
                ('accel', vec3b),
                ('orient', orient),
                ('gforce', vec3f)]

class classic_ctrl(Structure):
    _fields_ = [('btns', c_short),
                ('btns_held', c_short),
                ('btns_released', c_short),
                ('r_shoulder', c_float),
                ('l_shoulder', c_float),
                ('ljs', joystick),
                ('rjs', joystick)]

class guitar_hero_3(Structure):
    _fields_ = [('btns', c_short),
                ('btns_held', c_short),
                ('btns_released', c_short),
                ('whammy_bar', c_float),
                ('js', joystick)]

class expansion_union(Union):
    _fields_ = [('nunchuk', nunchuk),
                ('classic', classic_ctrl),
                ('gh3', guitar_hero_3)]

class expansion(Structure):
    _fields_ = [('type', c_int),
                ('u', expansion_union)]

class wiimote_state(Structure):
    _fields_ = [('exp_ljs_ang', c_float),
                ('exp_rjs_ang', c_float),
                ('exp_ljs_mag', c_float),
                ('exp_rjs_mag', c_float),
                ('exp_btns', c_ushort),
                ('exp_orient', orient),
                ('exp_accel', vec3b),
                ('exp_r_shoulder', c_float),
                ('exp_l_shoulder', c_float),
                ('ir_ax', c_int),
                ('ir_ay', c_int),
                ('ir_distance', c_float),
                ('orient', orient),
                ('btns', c_ushort),
                ('accel', vec3b)]

# The wiimote structure is OS-dependent.
if sys.platform.startswith('linux'):
    os_dependent = [('bdaddr', c_void_p), # FIXME: c_void_p is not correct.
                    ('out_sock', c_int),
                    ('in_sock', c_int),
                    ('bdaddr_str', c_char * 18)]
elif sys.platform.startswith('win32'):
    os_dependent = [('dev_handle', c_void_p),
                    ('hid_overlap', c_void_p * 5),
                    ('stack', c_int),
                    ('timeout', c_int),
                    ('normal_timeout', c_ubyte),
                    ('exp_timeout', c_ubyte)]
elif sys.platform.startswith('darwin'):
    os_dependent = [('device', c_void_p),
                    ('address', c_void_p),
                    ('inputCh', c_void_p),
                    ('outputCh', c_void_p),
                    ('disconnectionRef', c_void_p),
                    ('connectionHandler', c_void_p),
                    ('bdaddr_str', c_char * 18)]


class wiimote(Structure):
    _fields_ = [('unid', c_int),] + os_dependent + \
               [('state', c_int),
                ('leds', c_ubyte),
                ('battery_level', c_float),
                ('flags', c_int),
                ('handshake_state', c_ubyte),
                ('read_req', c_void_p),
                ('accel_calib', accel),
                ('exp', expansion),
                ('accel', vec3b),
                ('orient', orient),
                ('gforce', gforce),
                ('ir', ir),
                ('btns', c_ushort),
                ('btns_held', c_ushort),
                ('btns_released', c_ushort),
                ('orient_threshold', c_float),
                ('accel_threshold', c_int),
                ('lstate', wiimote_state),
                ('event', c_int),
                ('event_buf', c_ubyte * MAX_PAYLOAD),
                ('motion_plus_id', c_ubyte * 6)]

wiimote_p = POINTER(wiimote)
wiimote_pp = POINTER(wiimote_p)

event_cb_t = CFUNCTYPE(None, wiimote_p)
read_cb_t = CFUNCTYPE(None, wiimote_p, POINTER(c_ubyte), c_uint16)
ctrl_status_cb_t = CFUNCTYPE(None, wiimote_p, c_int, c_int, c_int, POINTER(c_int), c_float)
dis_cb_t = CFUNCTYPE(None, wiimote_p)

def is_pressed(dev, button):
    return dev.btns & button

def is_held(dev, button):
    return dev.btns_held & button

def is_released(dev, button):
    return dev.btns_released & button

def is_just_pressed(dev, button):
    return is_pressed(dev, button) and not is_held(dev, button)

def using_acc(wm):
    return wm.state & 0x020

def using_exp(wm):
    return wm.state & 0x040

def using_ir(wm):
    return wm.state & 0x080

def using_speaker(wm):
    return wm.state & 0x100

def is_led_set(dev, led):
    return dev.leds & led


# Load the wiiuse library.
LIB_DIR = os.path.dirname(__file__)
if sys.platform.startswith('linux'):
    lib_path = os.path.join(LIB_DIR, 'libwiiuse.so')
elif sys.platform.startswith('win32'):
    lib_path = os.path.join(LIB_DIR, 'wiiuse.dll')
elif sys.platform.startswith('darwin'):
    lib_path = os.path.join(LIB_DIR, 'libwiiuse.dylib')
log.info('Using wiiuse library "%s"', lib_path)
lib = ctypes.cdll.LoadLibrary(lib_path)


# Wiiuse external API functions
# wiiuse.c
version = lib.wiiuse_version
version.argtypes = ()
version.restype = c_char_p
init = lib.wiiuse_init
init.argtypes = (c_int,)
init.restype = wiimote_pp
disconnected = lib.wiiuse_disconnected
disconnected.argtypes = (wiimote_p,)
disconnected.restype = None
rumble = lib.wiiuse_rumble
rumble.argtypes = (wiimote_p, c_int)
rumble.restype = None
toggle_rumble = lib.wiiuse_toggle_rumble
toggle_rumble.argtypes = (wiimote_p,)
toggle_rumble.restype = None
set_leds = lib.wiiuse_set_leds
set_leds.argtypes = (wiimote_p, c_int)
set_leds.restype = None
motion_sensing = lib.wiiuse_motion_sensing
motion_sensing.argtypes = (wiimote_p, c_int)
motion_sensing.restype = None
status = lib.wiiuse_status
status.argtypes = (wiimote_p,)
status.restype = None
set_flags = lib.wiiuse_set_flags
set_flags.argtypes = (wiimote_p, c_int, c_int)
set_flags.restype = c_int
set_orient_threshold = lib.wiiuse_set_orient_threshold
set_orient_threshold.argtypes = (wiimote_p, c_float)
set_orient_threshold.restype = None

# connect.c
find = lib.wiiuse_find
find.argtypes = (wiimote_pp, c_int, c_int)
find.restype = c_int
connect = lib.wiiuse_connect
connect.argtypes = (wiimote_pp, c_int)
connect.restype = c_int
disconnect = lib.wiiuse_disconnect
disconnect.argtypes = (wiimote_p,)
disconnect.restype = None

# events.c
poll = lib.wiiuse_poll
poll.argtypes = (wiimote_pp, c_int)
poll.restype = c_int

# ir.c
set_ir = lib.wiiuse_set_ir
set_ir.argtypes = (wiimote_p, c_int)
set_ir.restype = None
set_ir_vres = lib.wiiuse_set_ir_vres
set_ir_vres.argtypes = (wiimote_p, c_uint, c_uint)
set_ir_vres.restype = None
set_ir_position = lib.wiiuse_set_ir_position
set_ir_position.argtypes = (wiimote_p, c_int)
set_ir_position.restype = None
set_aspect_ratio = lib.wiiuse_set_aspect_ratio
set_aspect_ratio.argtypes = (wiimote_p, c_int)
set_aspect_ratio.restype = None

class Wiimote(object):
    def __init__(self, controller):
        self.wiimotes = init(1)
        self.wiimote = self.wiimotes.contents
        self.controller = controller
        self.disconnected = False

    def connect(self):
        """Attempt connection to a Wiimote, timeout after 5 seconds.
        Return the number of Wiimotes successfully connected to. In this case,
        it will 1 or 0."""
        found = find(self.wiimotes, 1, 5)
        log.debug('Found %s remote(s)', found)
        if found:
            connected = connect(self.wiimotes, 1)
            log.debug('Connected to %s remote(s)', connected)
            return connected

    def poll(self):
        log.debug('Entering poll loop')
        # Enable motion sensing
        motion_sensing(self.wiimote, 1)
        start_time = time.time()
        # Set an initial inactivity timeout
        timeout = time.time() + TIMEOUT_SECONDS
        while True:
            # If the wiimote has timed out, disconnect.
            if time.time() > timeout:
                log.debug('Wiimote connection timed out')
                self.controller.wiimote_disconnected.emit()
            if not self.disconnected:
                if poll(self.wiimotes, 1):
                    current_time = time.time()
                    # The wiimote is active, reset the timeout
                    timeout = current_time + TIMEOUT_SECONDS
                    dev = self.wiimote.contents
                    # Update status of buttons, LEDs and battery level
                    status = {
                        'buttons': [],
                        'leds': [],
                        'battery_level': dev.battery_level,
                        'elapsed_time': current_time - start_time,
                        'accel': {'x': dev.accel.x,
                                  'y': dev.accel.y,
                                  'z': dev.accel.z}
                    }
                    start_time = current_time
                    for name, led in leds.items():
                        if is_led_set(dev, led):
                            status['leds'].append(led)
                    if dev.event == WIIUSE_EVENT:
                        if dev.btns:
                            for name, button in buttons.items():
                                if is_pressed(dev, button):
                                    status['buttons'].append(button)
                    elif (dev.event == WIIUSE_DISCONNECT or
                          dev.event == WIIUSE_UNEXPECTED_DISCONNECT):
                        log.debug('Wiimote disconnected')
                        self.controller.wiimote_disconnected.emit()
                    self.controller.status_update.emit(status)
            else:
                log.debug('Breaking from poll loop')
                # Disable motion sensing
                motion_sensing(self.wiimote, 0)
                break

    def set_leds(self, led_state):
        log.debug('Setting LED state to {:04b}'.format(led_state >> 4))
        set_leds(self.wiimote, led_state)

    def toggle_rumble(self):
        log.debug('Toggling rumble')
        toggle_rumble(self.wiimote)
