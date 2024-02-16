
import datetime
from pymongo import MongoClient


class mongoHelper():
    def __init__(self) -> None:
        self.mongodb = MongoClient('mongodb://localhost:27017/')
        self.database = self.mongodb['RadioEsculta']
        self.collectionRadioEsculta= self.database['Transcricao']


    def insert_data(self, file_name,md5 , transciption) -> None:
        data = {
                "file_name":file_name,
                "hash_md5":md5,
                "transcription":transciption,
                "send_telegram":False,
                "timestamp":datetime.datetime.now()
                }
        
        
        return self.collectionRadioEsculta.insert_one(data)