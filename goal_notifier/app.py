__author__ = 'marijn'

from pprint import pprint
import time
import logging
#logging.basicConfig()
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%H%M%S')
log = logging.getLogger(__name__)

from receiver import Receiver
from expressor import Expressor

def main():
    log.info("Starting")
    receiver = Receiver("../ga_config.json")
    receiver.connect_goal_sources()
    expresor = Expressor()
    try:
        log.info("first event")
        expresor.event_alert()
        time.sleep(1)
        log.info("second event")
        expresor.event_alert()
        for c in range(10):
            log.info("%d Sleeping", c)
            time.sleep(1)
    finally:
        expresor.stop()
    log.info("Ending")
