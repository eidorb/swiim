import logging
import view

log = logging.getLogger('swiim.' + __name__)

def start_application():
    log.info('Application starting')
    swiim_application = view.SwiimApplication()
    swiim_application.run()
    log.info('Application exiting')