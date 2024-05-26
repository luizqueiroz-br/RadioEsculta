import hashlib
import os
from Utils.Telegram import TelegramApi
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

from DataBase.mongohelper import mongoHelper
from MachineLearning.machinelearning import voiceModel
from Utils.gerenciadorlogger import Logando

class QueQueManeger:
    def __init__(self) -> None:
        self.log = Logando()
        self.log.info("iniciando QueQueManager")


class ManipuladorDeArquivos(FileSystemEventHandler):

    def __init__(self, type_operador) -> None:
        self.log = Logando()
        self.log.info("Iniciando ManipuladorDeArquivos")
        self.voice = voiceModel()
        self.telegram = TelegramApi()
        self.mon = mongoHelper()

        super().__init__()

    def on_created(self, event: FileSystemEvent) -> None:
        self.log.info(f"[ARQUIVO CRIADO] {event}")

        return super().on_created(event)

    def on_closed(self, event: FileSystemEvent) -> None:
        self.log.info(f"[ARQUIVO FECHADO] { event}")

        if event.src_path.endswith(".wav"):
            segments, info = self.voice.transcible(audio_path=event.src_path)
            string_audio = ""
            for segment in segments:
                string_audio += "%s " % (segment.text)

            self.mon.insert_data(event.src_path, string_audio, True)
            self.telegram.sendAudio(event.src_path, string_audio)

        return super().on_closed(event)


class Utils:
    def __init__(self) -> None:
        self.log = Logando()
        self.log.info("Iniciar Utils")

    def calculate_md5_file(self, file_path) -> None:
        hash_md5 = hashlib.md5()
        self.log.info(f"calculate md5 {file_audio}")

        with open(file_path, "rb") as file_audio:
            for fragment in iter(lambda: file_audio.read(512), b""):
                hash_md5.update(fragment)
        return hash_md5.hexdigest()

    def loadPathAudios(self, path, type=".wav") -> list:
        arquivos = [
            (
                os.path.join(path, arquivo),
                self.calculate_md5_file(os.path.join(path, arquivo)),
            )
            for arquivo in os.listdir(path)
            if arquivo.endswith(type)
        ]
        return arquivos

    def lenAudio(self, audio): ...

    def monitoraPasta(path): ...
