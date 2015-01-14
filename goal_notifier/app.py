__author__ = 'marijn'

import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

from notifier import Notifier

def main():
    log.info("Starting")
    notifier = Notifier()
    notifier.connect_goal_sources()
    log.info("Ending")

