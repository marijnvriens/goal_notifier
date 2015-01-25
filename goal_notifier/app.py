__author__ = 'marijn'

from pprint import pprint
import logging
import time
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

from receiver import Receiver


def main():
    log.info("Starting")
    receiver = Receiver("../ga_config.json")
    receiver.connect_goal_sources()
#    pprint(receiver.get_data())
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


import pykka
from pydub import AudioSegment, playback


class Expressor(object):
    def __init__(self):
        self._audio = AudioOutput.start()
    def event_alert(self):
        self._audio.tell({'do': 'play', 'sound_file': 'SeagullCall.wav'})
    def stop(self):
        self._audio.stop()

class AudioOutput(pykka.ThreadingActor):
    def on_receive(self, message):
        fn = "../sounds/%s" % message['sound_file']
        audio = AudioSegment.from_wav(fn)
        log.info("Pre play call")
        playback.play(audio)
        log.info("Post play call")