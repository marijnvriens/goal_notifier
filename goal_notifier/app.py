__author__ = 'marijn'

from pprint import pprint
import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

from receiver import Receiver

def main():
    log.info("Starting")
    receiver = Receiver("../ga_config.json")
    receiver.connect_goal_sources()
    pprint(receiver.get_data())
    log.info("Ending")

