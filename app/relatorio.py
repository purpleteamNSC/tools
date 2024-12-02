import os
from dotenv import load_dotenv
from helix import Helix_T
from pathlib import Path
from datetime import datetime
import time
from pprint import pprint
# from openpyxl import load_workbook

load_dotenv()

# FUNÇOES


def create_path_all(company):
    """
    Cria a pasta REM caso nao exista
    """  
    dir_atual = Path.cwd()
    pasta_rem = dir_atual / "app" / "rem"
    pasta_company = pasta_rem / company

    if not pasta_rem.exists():
        pasta_rem.mkdir()

    if not pasta_company.exists():
        pasta_company.mkdir()


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
        "start": f"{ano_atual}-{mes_atual}-01T00:00:00Z",  # year-month-01T00:00:00Z
        "end": f"{ano_atual}-{mes_atual}-{meses[str(mes_atual)]}T00:00:00Z",  # year-month-30T00:00:00Z
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
# query = 'has=metaclass | groupby meta_cbname'
# helix.post_search_archive(query, set_date())


# BUSCA O RESULTADO DE UMA PESQUISA FEITA
# result = helix.result_search_archive(19809)
# check = result['data'][0]['state']
# process = result['data'][0]['percentComplete']


# while True:
#     result = helix.result_search_archive(19809)
#     check = result['data'][0]['state']
#     process = result['data'][0]['percentComplete']

#     if check == 'completed':
#         print(check)
#         break
#     else:
#         print(process)
#         time.sleep(60)


# PROCESSAR OS DADOS DE RESULTADO
# result_pesquisa = helix.result_search_archive(19808)['results']['results']['aggregations'].items()
# # print(result['query'])
# # pprint(result['queryAST'])
# data = next((v['buckets'] for _, v in result_pesquisa if 'buckets' in v), None)
# pprint(data)


# FUNÇAO PARA CRIAR O XLS
# def create_xlsx(company):
    

#     dir_atual = Path.cwd()
#     pasta_rem = dir_atual / "app" / "rem"
#     pasta_company = pasta_rem / company


#     ...


def main(company):
    helix = Helix_T(os.getenv("helix_id"), os.getenv("client_id"), os.getenv("secret"), os.getenv("scope_helix"))
    create_path_all(company)
    # PROCESSAR OS DADOS DE RESULTADO
    result_pesquisa = helix.result_search_archive(19808)['results']['results']['aggregations'].items()
    data = next((v['buckets'] for _, v in result_pesquisa if 'buckets' in v), None)
    pprint(data)

main('EMPRESA-A')