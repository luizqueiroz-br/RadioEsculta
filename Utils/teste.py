import requests

import time
import pandas as pd

def send_location_via_api(token, chat_id, latitude, longitude, message):
        # Enviar a mensagem de texto
    url_message = f"https://api.telegram.org/bot{token}/sendMessage"
    message_data = {
        'chat_id': chat_id,
        'text': message
    }
    requests.post(url_message, data=message_data)
    url = f"https://api.telegram.org/bot{token}/sendLocation"
    payload = {
        'chat_id': chat_id,
        'latitude': latitude,
        'longitude': longitude
    }
    response = requests.post(url, data=payload)
    return response.json()

# Substitua 'YOUR_TOKEN' pelo seu token de bot e 'YOUR_CHAT_ID' pelo ID do chat
token = "661891149:AAHXbPBwMSR5ZIeySyPs-y4L4PvRvzJvozU"
chat_id = "-1002022196761"












# Caminho para o arquivo de dados
file_path = 'mnt/d/radio/gcm/DSDPlus.LRRP'

# Função para ler os dados e detectar novas linhas
def read_new_data(file_path, last_known_line=0):
    try:
        data = pd.read_csv(file_path, delimiter='\s+', header=0)
        if last_known_line < len(data):
            new_data = data.iloc[last_known_line:]
            return new_data, len(data)
        return None, last_known_line
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None, last_known_line

# Função para enviar mensagens no Telegram
def send_updates(data):
    for _, row in data.iterrows():
        print(row[1],row[2],row[3],row[4],row[5])
        msg = str(row[1])+' Viatura: '+str(row[2])+' long '+str(row[3])+' lat '+str(row[4])+' velocidade '+str(row[5])+'km'
        send_location_via_api(token, chat_id, row[3], row[4], msg)
        time.sleep(1)  # Intervalo para evitar spam

# Função principal que controla o fluxo
def main_loop():
    last_known_line = 0
    while True:
        new_data, last_known_line = read_new_data(file_path, last_known_line)
        if new_data is not None:
            send_updates(new_data)
        time.sleep(60)  # Espera 1 minuto antes da próxima checagem

if __name__ == "__main__":
    main_loop()
