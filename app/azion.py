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
            # print(res.json())
            return res.json()
        except:
            print(res.status_code)
            return res.status_code



# token = os.getenv('token_azion')

# hosts_waf_pnb_azion = os.getenv('hosts_waf_pnb_azion')
# white_list_pnb_azion = os.getenv('white_list_pnb_azion')


# azion = Azion(token)
# azion.get_list_azion(hosts_waf_pnb_azion)
# print('')
# azion.get_list_azion(white_list_pnb_azion)

