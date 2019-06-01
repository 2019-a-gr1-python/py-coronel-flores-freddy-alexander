# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:53:31 2019

@author: alex
"""
import pandas as pd 
import os 
path = '/home/alex/Documents/py-coronel-flores-freddy-alexander/03_Pandas/data/csv/artwork_data.csv'

pd.read_csv(path
            ,nrows=100,
            usecols=['id','artist'],
            index_col = 'id'
            )


columns_usar = ['id','artist','title','medium','year','acquisitionYear','year','width','height','units']


df_completo = pd.read_csv(path
            ,nrows=100,
            usecols=columns_usar,
            index_col = 'id'
            )
            
path_gurdar = '/home/alex/Documents/py-coronel-flores-freddy-alexander/03_Pandas/data/csv/artwork_data.pickle'


df_completo.to_pickle(path_gurdar)

df_completo_pickle = pd.read_pickle(path_gurdar)

df_completo.head()