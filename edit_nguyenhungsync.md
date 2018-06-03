# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

1. File client/speech/mic.py
	Comment line : 37 // disable API
	Comment line : 209 -> 2012 // disable get UID from conf cache
	SET : self.account_id = '0' on line 208
2. File client/speech/listener.py
	Line 258 : config LANG  pocketsphinx
3. File client/speech/listener.py
	Line 244 : emit hotword
4. File client/speech/hotword_factory.py		
	Line 68 : config phonemes pocketsphinx
5. File configuration/config.py
	Disable remote config
	Renew code
	Comment # REMOTE_CONFIG = "mycroft.ai"
	Comment # RemoteConf Class
6. File mycroft.conf 
	Edit lang for use STT , TTS, dialog , dialog skill
7. File client/speech/main.py
	Line 21 : Comment # from mycroft.identity import IdentityManager
	Line 102 - 103 : # def handle_paired(event):
					 #     IdentityManager.update(event.data)
	Line 156 : Comment # ws.on("mycroft.paired", handle_paired)
// Skill Folder Edited Start
8.   File skills/main.py
	Remove all API form mycroft API 
	Line 29 : Comment 
	  from mycroft.api import is_paired, BackendDown
	Line 107 - 110 : comment 
	  if is_paired():
            # Skip the sync message when unpaired because the prompt to go to
            # home.mycrof.ai will be displayed by the pairing skill
            enclosure.mouth_text(dialog.get("message_synching.clock"))

	Line : 147 - 161 : comment pair check:
	 try:
            if not is_paired(ignore_errors=False):
                payload = {
                    'utterances': ["pair my device"],
                    'lang': "en-us"
                }
                ws.emit(Message("recognizer_loop:utterance", payload))
            else:
                from mycroft.api import DeviceApi
                api = DeviceApi()
                api.update_version()
        except BackendDown:
            data = {'utterance': dialog.get("backend.down")}
            ws.emit(Message("speak", data))
            ws.emit(Message("backend.down"))
9. File Skills/Setting.py
	# Disabel Device API
	Line 66 : Comment # from mycroft.api import DeviceApi, is_paired 
	Line 88 : Comment s# self.api = DeviceApi()
	<!-- # STOP use Setting.py
		## Reason : sync with setting skill online ( not use )
		## Rename : Setting_disable.py --> Removed
10. File __init__.py
	# Disable # from mycroft.api import Api
11. File comguration/__init__py
	Remove from .config import Configuration, LocalConf, RemoteConf, \
	#                    SYSTEM_CONFIG, USER_CONFIG
	ADD :from .config import Configuration, LocalConf,SYSTEM_CONFIG, USER_CONFIG
12. File Skills/Core
	Line 31 : Comment # from mycroft.api import DeviceApi
	Line 441 : Comment # DeviceApi().send_email(title, body, basename(self.root_dir))
13. File client/enclosure/__init__.py
	Line 24 : Comment # from mycroft.api import has_been_paired
14. FIle /metrics/__init__.py"
	Line 21 : Comment # from mycroft.api import DeviceApi, is_paired
	Line 37 -> 42 : Comment
		# try:
    	#     if is_paired() and Configuration().get()['opt_in']:
    	#         DeviceApi().report_metric(name, data)
    	# except requests.RequestException as e:
    	#     LOG.error('Metric couldn\'t be uploaded, due to a network error ({})'
    	#               .format(e))
15. File SKill/core.py
	<!-- Line 39 : Comment # from mycroft.skills.settings import SkillSettings
	Line 210 : Comment # self.settings = SkillSettings(self._dir, self.name) --> Removed
16. File tts/__init__py
	Line 443 : Comment   # from mycroft.tts.mimic_tts import Mimic
	Line 439 : Comment   # "mimic": Mimic,
17. File sst/__init_py
	Line 22 : Comment # from mycroft.api import STTApi
	Line 124 -> 149 : Comment
# class MycroftSTT(STT):
#     def __init__(self):
#         super(MycroftSTT, self).__init__()
#         self.api = STTApi("stt")

#     def execute(self, audio, language=None):
#         self.lang = language or self.lang
#         try:
#             return self.api.stt(audio.get_flac_data(convert_rate=16000),
#                                 self.lang, 1)[0]
#         except:
#             return self.api.stt(audio.get_flac_data(), self.lang, 1)[0]


# class MycroftDeepSpeechSTT(STT):
#     """Mycroft Hosted DeepSpeech"""
#     def __init__(self):
#         super(MycroftDeepSpeechSTT, self).__init__()
#         self.api = STTApi("deepspeech")

#     def execute(self, audio, language=None):
#         language = language or self.lang
#         if not language.startswith("en"):
#             raise ValueError("Deepspeech is currently english only")
#         return self.api.stt(audio.get_wav_data(), self.lang, 1)

	Line 206 : Comment  # "mycroft": MycroftSTT,
