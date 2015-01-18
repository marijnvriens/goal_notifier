__author__ = 'marijn'

from goals import GaGoalSource

class Notifier(object):
    def __init__(self, ga_conf_filename):
        self._source = GaGoalSource(ga_conf_filename)

    def connect_goal_sources(self):
        self._source.connect()

    def get_data(self):
        return self._source.get_data_point('hr', 'goals')