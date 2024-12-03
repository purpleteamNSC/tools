import os
from dotenv import load_dotenv
from helix import Helix_T
from pathlib import Path
from datetime import datetime
import time
from pprint import pprint
from openpyxl import Workbook

load_dotenv()

helix = Helix_T(
    os.getenv("helix_id"),
    os.getenv("client_id"),
    os.getenv("secret"),
    os.getenv("scope_helix"),
)

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


def delete_all_archive():
    helix.delete_search_archive()


def criar_pesquisa(query, datas):
    # CRIA UMA PESQUISA EM ARCHIVE
    helix.post_search_archive(query, datas)


def verifica_result_archive(id):
    # BUSCA O RESULTADO DE UMA PESQUISA FEITA 19809

    result = helix.result_search_archive(id)
    check = result["data"][0]["state"]
    process = result["data"][0]["percentComplete"]

    results = {"result": result, "check": check, "process": process}

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

    return results


# PROCESSAR OS DADOS DE RESULTADO
# result_pesquisa = helix.result_search_archive(19808)['results']['results']['aggregations'].items()
# # print(result['query'])
# # pprint(result['queryAST'])
# data = next((v['buckets'] for _, v in result_pesquisa if 'buckets' in v), None)
# pprint(data)


# FUNÇAO PARA CRIAR O XLS
def create_xlsx(name, query, dados):
    # Extraindo as colunas do groupby na query
    groupby_part = [parte.strip() for parte in query.split("|") if "groupby" in parte][
        0
    ]
    colunas = (
        groupby_part.replace("groupby", "").strip().split()
    )  # Extraindo os nomes das colunas
    colunas.append("count")  # Adicionando a coluna "count"

    # Criando o arquivo Excel
    wb = Workbook()
    sheet = wb.active
    sheet.title = name

    # Adicionando cabeçalhos
    sheet.append(colunas)

    # Adicionando os valores
    for item in dados:
        # Preenche as colunas do groupby com valores da chave dinâmica (separadas por vírgulas)
        row = [item["key"]] + [None] * (len(colunas) - 2) + [item["doc_count"]]
        sheet.append(row)

    # Salvando o arquivo com o nome da tabela
    nome_arquivo = f"{name}.xlsx"
    wb.save(nome_arquivo)
    print(f"Tabela '{nome_arquivo}' criada com sucesso!")


def verifica_pa_all(query, datas):
    pa_all = helix.get_search_archive()  # pesquisas feitas em archives
    
    for pa in pa_all:
        print(pa['id'])
        if (
            pa["query"] == query
            and pa["searchStartDate"] == datas["start"]
            and pa["searchEndDate"] == datas["end"]
        ):
            
            return "ok"
        else:
            return "new"


# MAIN
def main(company):
    # helix = Helix_T(os.getenv("helix_id"), os.getenv("client_id"), os.getenv("secret"), os.getenv("scope_helix"))
    # delete_all_archive()
    create_path_all(company)
    datas = set_date()

    ps_all = helix.get_search_saved()  # pesquisas salvas

    for ps in ps_all:
        if verifica_pa_all(ps["query"], datas) == "new":
            print(f"Criando para {ps['name']}")
            # helix.post_search_archive(ps["query"], datas)

    # PROCESSAR OS DADOS DE RESULTADO
    # result_pesquisa = helix.result_search_archive(19808)['results']['results']['aggregations'].items()
    # data = next((v['buckets'] for _, v in result_pesquisa if 'buckets' in v), None)
    # create_xlsx(company, data)


main("EMPRESA-A")
