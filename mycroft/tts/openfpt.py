# Coppy right @2018 nguyenhungsync
# Donot coppy
import requests
from mycroft.configuration import Configuration
import vlc

from gtts import gTTS
from mycroft.util import (
    check_for_signal,
    get_ipc_directory,
    resolve_resource_file,
    play_wav
)
from mycroft.tts import TTS, TTSValidator


class FptTTS(TTS):
    def __init__(self, lang, config):
        super(FptTTS, self).__init__(lang, config, FptTTSValidator(
            self), 'mp3')
  # trỏ đến class mẹ của FPTTTS là TTS ( quy tắc kế thừa), lấy các giá trị lang, config, FPTSValidator
   # tương đương  TTS.__init__(lang, config, FptTTSValidator(self)
    # get lang, config và validator 
    # queue bằng định dạng mp3 
    # OPEN FPT use Mp3 format
    def execute(self, sentence, ident=None):
        # subprocess.call()
        url = "http://api.openfpt.vn/text2speech/v4"
        headers = {"api_key": "ccf7ec73230f4817be0a990cf7343dcc",
                   "voice" : "female",
                   "Cache - Control": "no - cache"}
        fpt_send = requests.post(url, headers=headers, data=sentence.encode('utf-8'))
        data_res = fpt_send.json()
        self.res = data_res['async']
        res = data_res['async']
        self.load_config = Configuration.get()
        if fpt_send.status_code == 200 :
            try:
                self.begin_audio()
                # file = resolve_resource_file("snd/wellcome.WAV")
                # play_wav(file)
                p = vlc.MediaPlayer(res)
                p.play()
            finally:
                self.end_audio()    
        # if fpt_send.status_code == 200 :
        #     print(data_res['async'])
        #     try:
        #         self.begin_audio()
        #         if self.config.get('confirm_listening'):
        #             file = resolve_resource_file(
        #                 self.config.get('sounds').get('start_listening'))
        #             if file:
        #                 play_wav(file)
        #     except Exception as e:
        #         LOG.error(e.message)
        #     finally:
        #         self.end_audio()    
        # self.end_audio()
    def ghi_file(self, data):
        with open(self.filename, 'wb') as f:
            f.write(data)

class FptTTSValidator(TTSValidator):
    def __init__(self, tts):
        super(FptTTSValidator, self).__init__(tts)

    def validate_lang(self):
        # TODO
        pass

    def validate_connection(self):
        pass

    def get_tts_class(self):
        return FptTTS


