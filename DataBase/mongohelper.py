import datetime

from pymongo import MongoClient


class mongoHelper:
    def __init__(self) -> None:
        self.mongodb = MongoClient("mongodb://localhost:27017/")
        self.database = self.mongodb["RadioEsculta"]
        self.collectionRadioEsculta = self.database["Transcricao"]

    def get_all_conversation(self):
        data = []
        for conve in self.collectionRadioEsculta.find({}):
            del conve['_id']
            data.append(conve)
        return data

    def insert_data(self, file_name, transciption, send_telegram) -> None:
        data = {
            "file_name": file_name,
            "transcription": transciption,
            "send_telegram": send_telegram,
            "timestamp": datetime.datetime.now(),
        }

        return self.collectionRadioEsculta.insert_one(data)
