from splinter import Browser
import datetime as dt
import time
import pandas as pd
import os

import colector

resp_1 = int(input('Criar novo arquivo (1) ou utilizar um existente (2)?: '))
if resp_1 == 1:
    filename = str(input('Coloque o nome do arquivo de saída: '))
    df = pd.DataFrame(columns=['velocidadeideal','fast','brasilBandaLarga','time'])
    df.to_csv('{}.csv'.format(filename))
elif resp_1 == 2:
    filename = str(input('Coloque o nome do arquivo existente: '))

i = 0

while True:
    try:
        i=i+1
        start = dt.datetime.now()
        colector.job(filename)
        print('Iter: {} | Tempo: {}'.format(i ,(dt.datetime.now() - start)))
        time.sleep(40)
    except:
        print('Deu ruim!! Reiniciando o processo...')
        time.sleep(5*60)