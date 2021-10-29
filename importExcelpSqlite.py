import pandas as pd
from Banco2 import Banco
from datetime import datetime, date

novovcto = []
novopgto = []
banco = Banco()
meses = ['Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
products = pd.DataFrame()

for mes in meses:


    df = pd.read_excel(
        'GERENCIADOR.xlsx', 
        sheet_name=mes,
        header=0)

    products = products.append(df)

    print(mes)


for linha in products['vcto']:
    # so para lembrar tipodedata = "+" + str(type(linha)) + "+"
    
    if type(linha) is datetime or str(type(linha)) == "<class 'pandas._libs.tslibs.timestamps.Timestamp'>":
        #data_hora_br = linha.strftime('%d/%m/%Y').format(date)

        novovcto.append(linha)
    else:
        vazia = ""
        novovcto.append(vazia)
        
        

del products['vcto']

products.insert(7, "vcto",novovcto, allow_duplicates=True)


for linha3 in products['pgto']:
   
    if type(linha3) is datetime or str(type(linha3)) == "<class 'pandas._libs.tslibs.timestamps.Timestamp'>":
        #data_hora_brpg = linha3.strftime('%d/%m/%Y').format(date)
        novopgto.append(linha3)
    else:
        vazia = ""
        novopgto.append(vazia)
        
del products['pgto']

products.insert(7, "pgto",novopgto, allow_duplicates=True)


c = banco.conexao
products.to_sql('controles', c, if_exists='append', index=False)




print("Final Feliz")