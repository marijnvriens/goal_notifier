__author__ = 'marijn'

from pprint import pprint
import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


from notifier import Notifier

def main():
    log.info("Starting")
    notifier = Notifier("../ga_config.json")
    notifier.connect_goal_sources()
    pprint(notifier.get_data())
    log.info("Ending")

