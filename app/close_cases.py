import time
import os
from helix import Helix_T
from dotenv import load_dotenv
load_dotenv()

# ENV

helix_id = os.getenv('helix_id')
client_id = os.getenv('client_id')
secret = os.getenv('secret')
scope = os.getenv('scope_helix')

x = Helix_T("x", helix_id, client_id, secret, scope)

data = x.get_cases()
limit = data['meta']['count']
cases = x.get_cases()['results']

while True:
    count = data['meta']['count']
    cases = x.get_cases()['results']

    if count != 0:
        for case in cases:
            x.delete_case(case['id'])

    if count == 0:
        print('Todos os casos foram deletados')
        time.sleep(3600)
