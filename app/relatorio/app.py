import os
from dotenv import load_dotenv
from app.umbrella import t_umbrella

load_dotenv()



# print(os.getenv('helix_id'))
t_umbrella()