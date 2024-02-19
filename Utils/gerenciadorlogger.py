import logging



class Logando():
    def __init__(self) -> None:
        logging.basicConfig(level=logging.INFO, format='[%(asctime)s] - [%(levelname)s] : %(message)s')
    
    def info(self, msg):
        logging.info(msg)

