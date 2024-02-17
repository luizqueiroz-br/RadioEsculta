#https://huggingface.co/Systran/faster-whisper-large-v3
from Utils.fileshelper import Utils
from DataBase.mongohelper import mongoHelper
from Utils.gerenciadorlogger import Logando

# mongo = mongoHelper()

# utils = Utils()
# for audio in utils.loadPathAudios('audios/'):
#     print('dialog, ', audio)
#     string_audio = ''
#     for segment in segments:
#         string_audio += "[%.2fs -> %.2fs] %s | " % (segment.start, segment.end, segment.text)
#     mongo.insert_data(file_name=audio[0],md5=audio[1],transciption=string_audio)
#     print(string_audio)


def main():
    log = Logando()
    log.info('iniciando os motores....')

if __name__ == '__main__':
    main()