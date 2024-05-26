import datetime

from pymongo import MongoClient


class mongoHelper:
    def __init__(self) -> None:
        self.mongodb = MongoClient("mongodb://localhost:27017/")
        self.database = self.mongodb["RadioEsculta"]
        self.collectionRadioEsculta = self.database["Transcricao"]
        self.collectionRadioTermos = self.database["TermosMonitorados"]

    def get_all_conversation(self, limit, skip):
        data = []
        for conve in self.collectionRadioEsculta.find({}).skip(skip).limit(limit):
            del conve["_id"]
            data.append(conve)
        # https://chatgpt.com/g/g-2DQzU5UZl-code-copilot/c/4920d31a-0d0e-47a3-871e-d689ea546062
        data.reverse()
        resultados = {"dados": data, "count": len(data)}
        return resultados

    def add_termo_monitorado(self, termo, canal_de_envio):
        data = {
            "termo": termo,
            "timestamp": datetime.datetime.now(),
            "canal_de_envio": canal_de_envio,
        }
        return self.collectionRadioTermos.insert_one(data)

    def get_termo_monitorado(self):
        return self.collectionRadioTermos.find({})

    def insert_data(
        self, file_name: str, transciption: str, send_telegram: bool
    ) -> None:
        data = {
            "file_name": file_name,
            "transcription": transciption,
            "send_telegram": send_telegram,
            "timestamp": datetime.datetime.now(),
        }

        return self.collectionRadioEsculta.insert_one(data)
