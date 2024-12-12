import requests
import os
from dotenv import load_dotenv


load_dotenv()


class Azion:
    def __init__(self, token) -> None:
        self.token = token


    def get_list_azion(self,list):
        url = f"https://api.azionapi.net/network_lists/{list}"

        headers = {
            "Accept": "application/json; version=3",
            "Authorization": f"Token {self.token}",
        }

        try:
            res = requests.get(url, headers=headers)
            print(res.json())
            return res.json()
        except:
            print(res.status_code)
            return res.status_code



token = os.getenv('token_azion')
list = os.getenv('azion_list')


azion = Azion(token)
azion.get_list_azion(list)

