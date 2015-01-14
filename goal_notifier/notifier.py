__author__ = 'marijn'

from goals import GaGoalSource

class Notifier(object):
    def __init__(self):
        self._source = GaGoalSource()

    def connect_goal_sources(self):
        self._source.connect()

