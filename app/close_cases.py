import time
import os
from helix import Helix_T, Helix_F
from dotenv import load_dotenv

load_dotenv()


# fecha todos os cases lado trellix
def close_cases_lt():

    # Instacia
    x = Helix_T(
        os.getenv("helix_id"),
        os.getenv("client_id"),
        os.getenv("secret"),
        os.getenv("scope_helix"),
    )

    while True:
        data = x.get_cases()
        count = data["meta"]["count"]
        cases = x.get_cases()["results"]

        if count != 0:
            for case in cases:
                x.delete_case(case["id"])

        if count == 0:
            print("Todos os casos foram deletados")
            time.sleep(3600)


# fecha todos os cases com declared lado fireeye
def close_cases_lf():

    # Instancia
    h = Helix_F(os.getenv("helix_id"), os.getenv("helix_api_key"))

    while True:
        data = h.get_cases()
        count = data["meta"]["count"]
        cases = data["results"]

        if count != 0:
            cases = data["results"]
            for case in cases:
                h.delete_case(case["id"])

        if count == 0:
            print("Todos os casos foram deletados")
            time.sleep(3600)
