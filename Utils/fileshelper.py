
import os
import hashlib
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from Utils.gerenciadorlogger import Logando
from MachineLearning.machinelearning import voiceModel
import requests

class TelegramApi():
    def __init__(self) -> None:
        self.bot_token = '661891149:AAHXbPBwMSR5ZIeySyPs-y4L4PvRvzJvozU'
        self.group_id = -926984022

    def sendAudio(self, path_audio, transcricao):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendAudio"

        try:
            with open(path_audio, 'rb') as f:
                files = {'audio': f}
                data = {'chat_id': self.group_id,
                        'caption': transcricao,
                        'parse_mode': 'HTML'
                        }
                response = requests.post(url, files=files, data=data)
                if response.status_code != 200:
                    print(f"Erro ao enviar áudio: {response.text}")
                else:
                    print(f"Áudio enviado: {path_audio}")
        except Exception as e:
            print(f"Erro: {e}")


class QueQueManeger():
    def __init__(self) -> None:
        self.log = Logando()
        self.log.info('iniciando QueQueManager')

class ManipuladorDeArquivos(FileSystemEventHandler):

    def __init__(self) -> None:
        self.log = Logando()
        self.log.info('Iniciando ManipuladorDeArquivos')
        self.voice = voiceModel()
        self.telegram = TelegramApi()
        super().__init__()

    def on_created(self, event: FileSystemEvent) -> None:
        self.log.info(f'[ARQUIVO CRIADO] {event}')

        return super().on_created(event)
    
    def on_closed(self, event: FileSystemEvent) -> None:
        self.log.info(f'[ARQUIVO FECHADO] { event}')

        if event.src_path.endswith('.wav'):
            segments, info = self.voice.transcible(audio_path=event.src_path)  
            string_audio = ''    
            for segment in segments:
                string_audio += "[%.2fs -> %.2fs] %s | " % (segment.start, segment.end, segment.text)
            self.telegram.sendAudio(event.src_path, string_audio)

        return super().on_closed(event)

class Utils():
    def __init__(self) -> None:
        self.log = Logando()
        self.log.info('Iniciar Utils')

    def calculate_md5_file(self, file_path) -> None:
        hash_md5 = hashlib.md5()
        self.log.info(f'calculate md5 {file_audio}')

        with open(file_path, "rb") as file_audio:
            for fragment in iter(lambda: file_audio.read(512), b""):
                hash_md5.update(fragment)
        return hash_md5.hexdigest()
        

    def loadPathAudios(self, path, type='.wav') -> list:
        arquivos = [(os.path.join(path,arquivo), self.calculate_md5_file(os.path.join(path,arquivo))) for arquivo in os.listdir(path) if arquivo.endswith(type)]
        return arquivos

    def lenAudio(self, audio):
        ...

    def monitoraPasta(path):
        ...
    
