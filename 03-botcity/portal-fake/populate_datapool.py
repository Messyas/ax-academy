import os
from dotenv import load_dotenv
import pandas as pd
from botcity.maestro import BotMaestroSDK
from botcity.maestro.datapool import DataPoolEntry

load_dotenv()

SERVER = os.getenv('MAESTRO_SERVER')
LOGIN = os.getenv('MAESTRO_LOGIN')
KEY = os.getenv('MAESTRO_KEY')
DATAPOOL = os.getenv('DATAPOOL_LABEL')
#PORTAL_URL = os.getenv('PORTAL_URL')
CSV = os.getenv('CSV_PATH')

# vamos nos autenticar...
maestro = BotMaestroSDK()
maestro.login(server=SERVER, login=LOGIN, key=KEY)

# buscar qual datapool...
datapool = maestro.get_datapool(label=DATAPOOL)
#vamos agora carregar os dados do csv ...
df = pd.read_csv(CSV, dtype=str)

#vamos ler linha por linha do csv carregado e mandar para o datapool
for _, row in df.iterrows():
    entry = DataPoolEntry(
        value=row.to_dict(),
        datapool_label=DATAPOOL,
        maestro=maestro,
    )
    #mandar os dados como PENDENTE...
    datapool.create_entry(entry)
    print(f"Adicionado: {row['nome']} {row['sobrenome']}")

print(f"Adicionado {len(df)} registros ...")