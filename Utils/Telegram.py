import requests

class TelegramApi:
    def __init__(self) -> None:
        self.bot_token = "661891149:AAHXbPBwMSR5ZIeySyPs-y4L4PvRvzJvozU"

    def sendAudio(self, path_audio, transcricao,group_id="-1002022196761"):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendAudio"

        try:
            with open(path_audio, "rb") as f:
                files = {"audio": f}
                data = {
                    "chat_id": group_id,
                    "caption": transcricao,
                    "parse_mode": "HTML",
                }
                response = requests.post(url, files=files, data=data)
                if response.status_code != 200:
                    print(f"Erro ao enviar áudio: {response.text}")
                else:
                    print(f"Áudio enviado: {path_audio}")
        except Exception as e:
            print(f"Erro: {e}")