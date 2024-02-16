
import os
import hashlib

class Utils():
    def __init__(self) -> None:
        pass

    def calculate_md5_file(self, file_path) -> None:
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as file_audio:
            for fragment in iter(lambda: file_audio.read(512), b""):
                hash_md5.update(fragment)
        return hash_md5.hexdigest()
        

    def loadPathAudios(self, path, type='.wav') -> list:
        arquivos = [(os.path.join(path,arquivo), self.calculate_md5_file(os.path.join(path,arquivo))) for arquivo in os.listdir(path) if arquivo.endswith(type)]
        return arquivos

    def lenAudio(self, audio):
        ...



