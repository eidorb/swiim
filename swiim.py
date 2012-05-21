import logging
import sys
from application.controller import start_application

log = logging.getLogger('swiim')

def main():
    setup_logging()
    start_application()
    sys.exit()

def setup_logging():
    """Set up logging. Uses a StreamHandler to log to the console"""

    formatter = logging.Formatter('%(name)s %(levelname)s: %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    log.setLevel(logging.DEBUG)
    log.addHandler(console_handler)

if __name__ == '__main__':
    main()