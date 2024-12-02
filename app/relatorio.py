import os
from dotenv import load_dotenv
from helix import Helix_T
from pathlib import Path
from datetime import datetime

load_dotenv()


helix_id = os.getenv("helix_id")
client_id = os.getenv("client_id")
secret = os.getenv("secret")
api_key = os.getenv("trellix_api_key")
scope = os.getenv("scope_helix")

helix = Helix_T(helix_id, client_id, secret, scope)

token = helix.get_access_token()

# FUNÇOES


# Cria a pasta REM caso nao exista
dir_atual = Path.cwd()
pasta_rem = dir_atual / "app" / "rem"


def create_path_rem():
    if not pasta_rem.exists():
        pasta_rem.mkdir()


def set_date():
    data_atual = datetime.now()
 
    mes_atual = data_atual.month 
    ano_atual = data_atual.year

    meses = {
        "1": 31,
        "2": 28,
        "3": 31,
        "4": 30,
        "5": 31,
        "6": 30,
        "7": 31,
        "8": 31,
        "9": 30,
        "10": 31,
        "11": 30,
        "12": 31,
    }


    if mes_atual == 1:
        mes_atual = 12
        ano_atual -= 1
    else:
        mes_atual -= 1

    datas = {
        "start" : f"{ano_atual}-{mes_atual}-01T00:00:00Z", # year-month-01T00:00:00Z
        "end" : f"{ano_atual}-{mes_atual}-{meses[str(mes_atual)]}T00:00:00Z" # year-month-30T00:00:00Z
    }

    return datas


# RDN

# PEGA TODAS AS PESQUISAS SALVAS
# pesquisas = helix.get_search_saved()

# for pesquisa in pesquisas:
#     print(f"{pesquisa['name']}")
#     print(f"{pesquisa['id']} - {pesquisa['query']}" )
#     print('')

# PEGA TODAS AS PESQUISAS FEITAS NO ARCHIVE
# pesquisas_feitas = helix.get_search_archive()
# print(pesquisas_feitas)

# DELETA TODOS AS PESQUISAS NO ARCHIVE
# delete_all = helix.delete_search_archive()

# if delete_all == 204:
#     print("Zerado")
# else:
#     print("Error")

# CRIA UMA PESQUISA EM ARCHIVE
# query = 'has=class | groupby class'
# helix.post_search_archive(query, set_date())


# # print(set_date())
# datas = set_date()
# print(datas['start'])

