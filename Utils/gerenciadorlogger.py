import logging



class Logando():
    def __init__(self) -> None:
        logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] - [%(levelname)s] : %(message)s')
    
    def info(self, msg):
        logging.info(msg)

