import pandas as pd
import folium
import requests
from PIL import Image
from io import BytesIO

# Função para ler e processar as últimas 5 linhas do arquivo
def process_data(file_path):
    data = pd.read_csv(file_path, delimiter='\s+', header=0)
    last_five = data.tail(5)
    return last_five

# Função para criar um mapa e plotar os pontos
def create_map(data):
    # Centrar o mapa na média das localizações
    center_lat = data['lat'].mean()
    center_long = data['long'].mean()
    map = folium.Map(location=[center_lat, center_long], zoom_start=12)

    # Adicionar marcadores para cada ponto
    for _, row in data.iterrows():
        folium.Marker([row[3], row[4]], popup=f"ID: {row[2]} Vel: {row[5]}").add_to(map)

    # Salvar o mapa como HTML e converter para PNG
    map.save('map.html')
    return 'map.html'

# Função para enviar a imagem do mapa para o Telegram
def send_map(token, chat_id, map_file):
    # Converte o HTML para uma imagem (exige ferramentas adicionais ou um serviço web)
    # Exemplo genérico aqui: Você precisa substituir essa lógica pela sua solução de conversão
    image = Image.open(map_file)
    byte_io = BytesIO()
    image.save(byte_io, 'PNG')
    byte_io.seek(0)

    url = f"https://api.telegram.org/bot{token}/sendPhoto"
    files = {'photo': byte_io}
    data = {'chat_id': chat_id}
    response = requests.post(url, data=data, files=files)
    print(response.json())

# Exemplo de uso
file_path = 'mnt/d/radio/gcm/DSDPlus.LRRP'
token = "661891149:AAHXbPBwMSR5ZIeySyPs-y4L4PvRvzJvozU"
chat_id = "-1002022196761"

data = process_data(file_path)
map_file = create_map(data)
send_map(token, chat_id, map_file)
