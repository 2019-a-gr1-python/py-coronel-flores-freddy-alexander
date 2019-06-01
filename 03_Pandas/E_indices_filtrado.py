# -*- coding: utf-8 -*-
"""
Created on Wed May 29 07:21:22 2019

@author: alex
"""

path = '/home/alex/Documents/py-coronel-flores-freddy-alexander/03_Pandas/data/csv/artwork_data.pickle'
import pandas as pd 
df_completo = pd.read_pickle(path)
serie_duplicados = df_completo['artist']
serie_artista = pd.unique(serie_duplicados)
serie_artista.size
blake = df_completo['artist']=='Blake,William'

df_blake = df_completo[blake]
