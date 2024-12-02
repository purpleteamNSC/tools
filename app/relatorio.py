import os
from dotenv import load_dotenv
from helix import Helix_T
from pathlib import Path

load_dotenv()


helix_id = os.getenv("helix_id")
client_id = os.getenv("client_id")
secret = os.getenv("secret")
api_key = os.getenv("trellix_api_key")
scope = os.getenv("scope_helix")

helix = Helix_T(helix_id,client_id,secret,scope)

token = helix.get_access_token()

# FUNÇOES


# Cria a pasta REM caso nao exista 
dir_atual = Path.cwd()
pasta_rem = dir_atual / 'app' / 'rem'

def create_path_rem():
    if not pasta_rem.exists():
        pasta_rem.mkdir()


# RDN
# pesquisas = helix.get_search_saved()

# for pesquisa in pesquisas:
#     print(f"{pesquisa['name']}")
#     print(f"{pesquisa['id']} - {pesquisa['query']}" )
#     print('')


# pesquisas_feitas = helix.get_search_archive()
# print(pesquisas_feitas)

# delete_all = helix.delete_search_archive()

# if delete_all == 204:
#     print('Zerado')
# else:
#     print('Error')