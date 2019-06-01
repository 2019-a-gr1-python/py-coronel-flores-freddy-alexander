# -*- coding: utf-8 -*-
"""
Created on Wed May 29 07:36:06 2019

@author: alex
"""


path = '/home/alex/Documents/py-coronel-flores-freddy-alexander/03_Pandas/data/csv/artwork_data.pickle'
import pandas as pd 
df = pd.read_pickle(path)
primero = df.loc[1035,'artist']

primero_a = df.iloc[0,1]

quese_a = df.iloc[[1,3,4],[1,2]]
a = df['width'].sort_values()

tres_primeros = df.head(10)['width'].sort_values(ascending=False).head(3)
tres_ultimos = df.head(10)['width'].sort_values().tail(3)

df_valido = pd.to_numeric(df['width'],errors='coerce')

df.loc[:,'width'] = df_valido

df_serie = pd.to_numeric(df['height'],errors='coerce')

df.loc[:,'height'] = df_serie

