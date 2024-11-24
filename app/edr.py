import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()


# resgata o token para (dev e ap)
def retrieve_access_token(client_id, client_secret, scope):
    url = "https://iam.cloud.trellix.com/iam/v1.1/token"
    # url = "https://auth.trellix.com/auth/realms/IAM/protocol/openid-connect/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": "client_credentials", "scope": scope}

    try:
        response = requests.post(
            url,
            headers=headers,
            data=data,
            auth=HTTPBasicAuth(client_id, client_secret),
        )
        # Verifica se a resposta é bem-sucedida
        response.raise_for_status()
        print(response.json())
        return response.json().get("access_token")  # Retorna o token de acesso
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Erro de HTTP
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")  # Outros erros de requisição
    except Exception as e:
        print(f"An error occurred: {e}")  # Qualquer outro erro


# resgata o token para (mgm)
def retrieve_token_mgm(client_id, client_secret):
    url = "https://auth.trellix.com/auth/realms/IAM/protocol/openid-connect/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            data=data,
            auth=HTTPBasicAuth(client_id, client_secret),
        )
        response.raise_for_status()  # Levanta uma exceção se o código de status for um erro
        print(response.json())
        return response.json().get("access_token")  # Retorna o token de acesso
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Erro de HTTP
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")  # Outros erros de requisição
    except Exception as e:
        print(f"An error occurred: {e}")  # Qualquer outro erro


# Chamadas
print("Client Credentials Management")
token_response1 = retrieve_token_mgm(
    os.getenv("mgm_client_id"), os.getenv("mgm_client_secret")
)
print()

print("Dev")
token_response2 = retrieve_access_token(
    os.getenv("dev_client_id"), os.getenv("dev_client_secret"), os.getenv("scope")
)
