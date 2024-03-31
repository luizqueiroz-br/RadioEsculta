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
        
        data.reverse()
        resultados = {"dados": data,
                    "count": len(data)}
        return resultados

    def insert_data(self, file_name: str, transciption: str, send_telegram: bool) -> None:
        data = {
            "file_name": file_name,
            "transcription": transciption,
            "send_telegram": send_telegram,
            "timestamp": datetime.datetime.now(),
        }

        return self.collectionRadioEsculta.insert_one(data)
