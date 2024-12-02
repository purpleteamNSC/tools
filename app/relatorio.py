import os
from dotenv import load_dotenv
from helix import Helix_T

load_dotenv()


helix_id = os.getenv("helix_id")
client_id = os.getenv("client_id")
secret = os.getenv("secret")
api_key = os.getenv("trellix_api_key")
scope = os.getenv("scope_helix")

helix = Helix_T(helix_id,client_id,secret,scope)

token = helix.get_access_token()

print(token)