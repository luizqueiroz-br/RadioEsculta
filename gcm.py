# https://huggingface.co/Systran/faster-whisper-large-v3
import time

from watchdog.observers import Observer

from DataBase.mongohelper import mongoHelper
from Utils.fileshelper import ManipuladorDeArquivos, Utils
from Utils.gerenciadorlogger import Logando

observer = Observer()


def main():
    log = Logando()
    log.info("iniciando os motores....")
    caminho = "audios/gcm"
    event_handler = ManipuladorDeArquivos()
    observer.schedule(event_handler, caminho, recursive=True)
    observer.start()


if __name__ == "__main__":
    main()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
