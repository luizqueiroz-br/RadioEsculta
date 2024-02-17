from faster_whisper import WhisperModel


class voiceModel():
    def __init__(self) -> None:
        self.model = WhisperModel("large-v3")


    def transcible(self, audio_path):
        
        segments, info = self.model.transcribe(audio=audio_path, language='pt')
        return segments, info

