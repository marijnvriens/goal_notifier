__author__ = 'marijn'

import logging
log = logging.getLogger(__name__)

import pykka
from pydub import AudioSegment, playback


class Expressor(object):
    def __init__(self):
        self._audio = AudioOutput.start()
    def event_alert(self):
        self._audio.tell({'do': 'play', 'sound_file': 'SeagullCall.wav'})
    def stop(self):
        log.warn("Stopping audio threads")
        self._audio.stop()


class AudioOutput(pykka.ThreadingActor):
    def on_receive(self, message):
        fn = "../sounds/%s" % message['sound_file']
        audio = AudioSegment.from_wav(fn)
        log.info("Pre play call")
        playback.play(audio)
        log.info("Post play call")