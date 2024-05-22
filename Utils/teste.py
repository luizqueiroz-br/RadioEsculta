import time

import pandas as pd
import requests

# Configurações do Mapbox
ACCESS_TOKEN = "pk.eyJ1IjoicXVlaXJvenZhbGUiLCJhIjoiY2pwZGhoMGNhMDNvbDNyazIwM3ViMzI0biJ9.fFw10jxOAWBYUZA_Nbd1JA"  # Substitua pelo seu token de acesso
STYLE = "mapbox/streets-v11"  # Escolha o estilo do mapa desejado


file_path = "/mnt/d/radio/gcm/DSDPlus.LRRP"
TOKEN = "661891149:AAHXbPBwMSR5ZIeySyPs-y4L4PvRvzJvozU"
CHAT_ID = "-1002022196761"


def get_color_code(velocity):
    # Retorna a cor do marcador em código hexadecimal (sem o '#')
    if velocity > 50:
        return "FF0000"  # Vermelho
    elif velocity > 20:
        return "0000FF"  # Azul
    else:
        return "00FF00"  # Verde


def get_color_by_id(id):

    data = {
        1043: "e41621",
        1036: "49bb96",
        1025: "e70cff",
        1033: "f9c45e",
        1042: "671837",
        1047: "b8a23e",
        1037: "5fcd3d",
        1029: "4b4851",
        1030: "37c7b0",
        1038: "ed5fa2",
        1007: "758527",
        1049: "5dbe94",
        2003: "c909a6",
        1039: "8caf73",
        1027: "80aa3c",
        1022: "df89ba",
        1009: "bfa07a",
        1012: "e29eb3",
        1018: "c06916",
        1032: "1692e3",
        1024: "c4243f",
        1019: "8e41ad",
        1031: "c5f9a7",
        1016: "05be41",
        1010: "72ed96",
        1028: "23cd20",
        1023: "65c199",
        1003: "255dfe",
        1021: "199b50",
        1026: "1675c9",
        1014: "1f95d9",
        1005: "64deb1",
        1051: "ccfc84",
    }
    try:
        return data[id]
    except Exception as e:
        print(e)
        return "00FF00"  # Verde


# Função para ler e processar os dados
def process_data(file_path):
    data = pd.read_csv(
        file_path,
        delimiter="\s+",
        header=None,
        names=["Data", "Hora", "id", "lat", "long", "velocidade", "direção"],
    )
    return data.tail(50)  # Retorna as últimas 5 entradas


# Função para gerar a imagem do mapa usando Mapbox com múltiplos marcadores
def fetch_map_image(data, size="800x800"):
    # Preparar string de marcadores
    markers = ",".join(
        [
            f'pin-l+{get_color_by_id(row["id"])}({row["long"]},{row["lat"]})'
            for index, row in data.iterrows()
        ]
    )
    center_lon = data["long"].mean()
    center_lat = data["lat"].mean()
    zoom = 12
    url = f"https://api.mapbox.com/styles/v1/{STYLE}/static/{markers}/{center_lon},{center_lat},{zoom}/{size}?access_token={ACCESS_TOKEN}"
    response = requests.get(url)
    if response.status_code == 200:
        with open("map.png", "wb") as f:
            f.write(response.content)
        return "map.png"
    else:
        print("Falha ao buscar a imagem do mapa:", response.status_code)
        print(response.content)
        return None


# Função para enviar a imagem do mapa para o Telegram
def send_map(token, chat_id, map_file, data):
    url = f"https://api.telegram.org/bot{token}/sendPhoto"
    with open(map_file, "rb") as image_file:
        files = {"photo": image_file}
        data = {
            "chat_id": chat_id,
            "caption": f"Verde < de 20 km Azul + de 20 km  vermelho + de 50 km: ",
            "parse_mode": "Markdown",
        }
        response = requests.post(url, data=data, files=files)
        print("Mapa enviado, resposta do servidor:", response.json())


# Função principal que controla o fluxo
def main_loop():
    while True:
        data = process_data(file_path)
        if not data.empty:
            try:
                map_file = fetch_map_image(data)
                if map_file:
                    send_map(TOKEN, CHAT_ID, map_file, str(data))
            except Exception as e:
                print(e)
        else:
            print("Nenhum dado novo para processar.")
        time.sleep(400)  # Pausa de 5 minutos


if __name__ == "__main__":
    main_loop()
