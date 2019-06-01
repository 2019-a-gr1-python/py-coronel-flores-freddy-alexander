# -*- coding: utf-8 -*-
"""
Created on Wed May 22 08:33:52 2019

@author: alex
"""

# 324
import json 
import pandas as pd 
import os 

path = '/home/alex/Documents/py-coronel-flores-freddy-alexander/03_Pandas/data/artwork/'
archivo = 'a/000/a00001-1035.json'
path_archivo = path+archivo
llaves = ['id','all_artists','title','medium','dateText','acquisitionYear',
          'wid','height','units']
registros = []
with open(path_archivo) as txt_json:
    contenido_json = json.load(txt_json)
    
    print(contenido_json)
    print(type(contenido_json))
    registros_df = []
    for llave in llaves:
        valor = contenido_json[llave]
        registros_df.append(llave)
    serie = tuple(registros_df)
    
    print(serie)
    