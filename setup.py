__author__ = 'marijn'

from setuptools import setup

setup(
    name="goal_notifier",
    version="0.0.0",
    license="AGPL3",
    packages=['goal_notifier'],
    requires=[
        "google-api-python-client",
        "pykka",
        "pydub",
        "pyopenssl",
    ],
    scripts=["goal_notifier"]
)