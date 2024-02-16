#https://huggingface.co/Systran/faster-whisper-large-v3
from faster_whisper import WhisperModel
from fileshelper import Utils
from mongohelper import mongoHelper

model = WhisperModel("large-v3")
mongo = mongoHelper()

utils = Utils()
for audio in utils.loadPathAudios('./')[:1]:
    print('dialog, ', audio)
    segments, info = model.transcribe(audio=audio, language='pt')
    string_audio = ''
    for segment in segments:
        string_audio += "[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text)
    print(string_audio)