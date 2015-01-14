__author__ = 'marijn'

import json

from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials
from httplib2 import Http


class GaGoalSource(object):
    """
    I am the source of events from Google Analytics.
    """
    def __init__(self):
        self._service = None

    def _create_service(self):
        with open("../Event Announce-eed13f51e563.json") as f:
            tokens = json.load(f)
        credentials = SignedJwtAssertionCredentials(tokens['client_email'], tokens['private_key'],
                                                    'https://www.googleapis.com/auth/analytics.readonly')
        # print(credentials)
        http = Http()
        credentials.authorize(http)
        self._service = build('analytics', 'v3', http=http)

    def connect(self):
        self._create_service()
        #self._service.management().accounts().list().execute()

        print(self._service.data().realtime().get(ids="ga:3893420", metrics="rt:activeUsers").execute())

        print(self._service.data().realtime().get(ids="ga:3893420", metrics="rt:goalCompletionsAll", dimensions="rt:goalId").execute())