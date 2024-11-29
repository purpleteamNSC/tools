import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

class Umbrella:
    def __init__(self, client_id, client_secret):
        self.base_url = 'https://api.umbrella.com'
        self.client_id = client_id
        self.client_secret = client_secret


    # token
    def get_token(self):
        url = 'https://api.umbrella.com/auth/v2/token'

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        response = requests.post(url, headers=headers, auth=HTTPBasicAuth(self.client_id, self.client_secret))
        response_json = response.json()
        token = response_json['access_token']
        return token


    # pega todas as redes criadas
    def get_networks(self):
        resource = '/deployments/v2/networks'

        url = self.base_url + resource

        headers = {
            'Authorization': f'Bearer {self.get_token()}',
            'Content-Type': 'application/json'
        }

        response = requests.get(url=url, headers=headers)

        data = response.json()

        print(data)
    

    # cria uma nova rede 
    def set_networks(self,name):
        resource = '/deployments/v2/networks'

        url = self.base_url + resource

        headers = {
            'Authorization': f'Bearer {self.get_token()}',
            'Content-Type': 'application/json'
        }

        data = {
            'name': f'{name}',
            'prefixLength': 32,
            'isDynamic': 'true',
            'status': 'OPEN'
        }

        response = requests.post(url=url, headers=headers, json=data)

        data = response.json()

        print(data)




# u = Umbrella(os.getenv('umbrella_key'),os.getenv('umbrella_secret'))

# print(u.get_token())
# # u.get_networks()

def t_umbrella():
    print('umbrella.py')

t_umbrella()
