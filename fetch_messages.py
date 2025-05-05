import requests
import json

import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do arquivo .env

SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

url = 'https://slack.com/api/conversations.history'

headers = {
    'Authorization': f'Bearer {SLACK_BOT_TOKEN}'
}

params = {
    'channel': CHANNEL_ID,
    'limit': 10  # Pega as 10 últimas mensagens
}

response = requests.get(url, headers=headers, params=params)


if response.status_code == 200:
    data = response.json()
    if data.get('ok'):
        messages = data.get('messages', [])
        print(f"\nÚltimas {len(messages)} mensagens no canal:\n")
        for msg in messages:
            user = msg.get('user', 'Desconhecido')
            text = msg.get('text')
            print(f"User: {user} - Mensagem: {text}")
    else:
        print("Erro na resposta da API:", data)
else:
    print(f"Erro HTTP: {response.status_code}")
