import os
import requests
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()


# Helix lado Trellix
class Helix_T:
    def __init__(self, helix_id, client_id, secret, scope):
        self.base_url = "https://apps.fireeye.com"
        self.helix_id = helix_id
        self.client_id = client_id
        self.secret = secret
        self.scope = scope

    def get_access_token(self):
        url = "https://auth.trellix.com/auth/realms/IAM/protocol/openid-connect/token"

        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        data = {"grant_type": "client_credentials", "scope": self.scope}

        auth = (self.client_id, self.secret)

        try:
            response = requests.post(url, headers=headers, auth=auth, data=data)
            response.raise_for_status()

            return response.json()["access_token"]
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")

        return None

    def get_alerts(self):
        """
        Função genérica para fazer requisições GET.
        """
        url = f"https://xdr.trellix.com/helix/id/{
            self.helix_id}/api/v1/alerts/"
        try:
            headers = {
                "x-trellix-api-token": f"Bearer {self.get_access_token()}",
                "accept": "application/json",
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")

        return None

    def get_cases(self):
        """
        Função genérica para fazer requisições GET.
        """
        url = f"https://xdr.trellix.com/helix/id/{self.helix_id}/api/v3/cases/"
        try:
            headers = {
                "x-trellix-api-token": f"Bearer {self.get_access_token()}",
                "accept": "application/json",
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")

        return None

    def delete_case(self, id):
        """
        Deletar um case
        """
        url = f"https://xdr.trellix.com/helix/id/{
            self.helix_id}/api/v3/cases/{id}"
        try:
            headers = {
                "x-trellix-api-token": f"Bearer {self.get_access_token()}",
                "accept": "application/json",
            }
            response = requests.delete(url, headers=headers)

            if response.status_code == 204:
                print("Caso excluido com sucesso")

            response.raise_for_status()
            return response.status_code
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")

        return None


# Helix lado Fireeye
class Helix_F:
    def __init__(self, helix_id, api):
        self.helix_id = helix_id
        self.api = api
        self.url = "https://apps.fireeye.com"

    # pega todos os cases com status Declared
    def get_cases(self):
        """
        Pega um case
        """
        url = f"{self.url}/helix/id/{self.helix_id}/api/v3/cases/"
        try:
            headers = {
                "x-fireeye-api-key": self.api,
                "accept": "application/json",
            }

            payload = {"status": "Declared"}

            response = requests.get(url, headers=headers, params=payload)

            # if response.status_code == 200:
            #     print(response.json())

            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")

        return None

    # Deleta um case
    def delete_case(self, id):
        """
        Deleta um case
        """
        url = f"{self.url}/helix/id/{self.helix_id}/api/v3/cases/{id}"
        try:
            headers = {
                "x-fireeye-api-key": self.api,
                "accept": "application/json",
            }
            response = requests.delete(url, headers=headers)

            if response.status_code == 204:
                print("Excluido com sucesso")

            return response.status_code
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")

        return None
