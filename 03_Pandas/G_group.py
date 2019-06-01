# -*- coding: utf-8 -*-
"""
Created on Wed May 29 08:23:00 2019

@author: alex
"""
import numpy as np
import math 
path = '/home/alex/Documents/py-coronel-flores-freddy-alexander/03_Pandas/data/csv/artwork_data.pickle'
import pandas as pd 

df = pd.read_pickle(path)

seccion_df = df.iloc[49980:50019,:].copy() 

df_group = seccion_df.groupby('acquisitionYear')

type(df_group)

def llenar_valores_vacios(serie):
    valores = series.value_counts()
    if(valores.empty):
        return valores
    

