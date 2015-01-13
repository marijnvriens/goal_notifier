__author__ = 'marijn'

import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

def main():
    log.info("Starting")
    log.info("Ending")

class GoalNotifier(object):
    pass