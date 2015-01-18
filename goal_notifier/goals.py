__author__ = 'marijn'

import json

from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials
from httplib2 import Http

import logging
log = logging.getLogger(__name__)

class GaGoalSource(object):
    """
    I am the source of events from Google Analytics.
    """

    segments_GA_calls = {
        'activeUsers': {'metrics': "rt:activeUsers"},
        'goals': {'metrics': "rt:goalCompletionsAll", 'dimensions': "rt:goalId"}
    }

    def __init__(self, ga_conf_filename):
        self._ga_conf_filename = ga_conf_filename
        self._service = None
        self.segments_GA_profiles = None

    def _create_service(self):
        '''
        Creates the authenticated Google Analytics object.
        :return: the service object
        '''
        with open(self._ga_conf_filename) as f:
            tokens = json.load(f)
            self.segments_GA_profiles = tokens['ga_profiles']
        credentials = SignedJwtAssertionCredentials(tokens['client_email'], tokens['private_key'],
                                                    'https://www.googleapis.com/auth/analytics.readonly')
        # print(credentials)
        http = Http()
        credentials.authorize(http)
        return build('analytics', 'v3', http=http)

    def connect(self):
        self._service = self._create_service()

    def available_events(self):
        return (
            ('hr', 'goals'),
        )

    def available_levels(self):
        return (
            ('hr', 'activeUsers')
        )

    def get_data_point(self, segment, values):
        args = {'ids': self.segments_GA_profiles[segment]}
        args.update(self.segments_GA_calls[values])
        res = self._service.data().realtime().get(**args).execute()
        log.debug("Raw GA result: %s", res)
        return self._make_data_points(res)

    def _make_data_points(self, results):
        source = results['profileInfo']['profileId']
        field_names = [f['name'] for f in results['columnHeaders']]
        dp = DataPoint(source, field_names)
        for r in results['rows']:
            dp.add_result(r)
        return dp


class DataPoint(object):
    def __init__(self, source, field_names):
        self._source = source
        self._field_names = field_names
        self._result_list = []

    def add_result(self, values):
        self._result_list.append(values)
