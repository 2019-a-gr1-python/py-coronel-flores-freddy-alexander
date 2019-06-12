# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 07:23:35 2019

@author: alex
"""
import pandas as pd
import numpy as np 
import os 
import sqlite3

path_guardado = '/home/alex/Documents/py-coronel-flores-freddy-alexander/03_Pandas/data/csv/artwork_data.pickle'
df_completo_pickle = pd.read_pickle(path_guardado)
df_completo_pickle.head()
df  = df_completo_pickle.iloc[50:200,:].copy()
df.head() 
path_a_guardar = '/home/alex/Documents/py-coronel-flores-freddy-alexander/03_Pandas/'

df.to_excel('ejemplo_basico.xlsx')
df.to_excel('ejemplo_basico_sin_indices.xlsx',index=False)
columns = ['artist','title','year']
df.to_excel('columns.xlsx',columns = columns)

# muliples hojas 

writer = pd.ExcelWriter('multiples_worksheet.xlsx',
                        engine="xlsxwriter")
df.to_excel(writer,sheet_name="Preview")
df.to_excel(writer,sheet_name="Preview 2",index=False)

df.to_excel(writer,sheet_name="Preview tres",columns = columns)
writer.save()
                
# formateo condicional 
artistas_contados = df_completo_pickle['artist'].value_counts()

writer = pd.ExcelWriter('colores.xlsx',engine='xlsxwriter')

artistas_contados.to_excel(writer,sheet_name='Artistas_contados')
hoja_artistas = writer.sheets['Artistas_contados']
rango_celdas = 'B2:B{}'.format(len(artistas_contados.index))

formato = {
    'type':'2_color_scale',
    'min_value':'10',
    'min_type':'percentile',
    'max_value': '99',
    'max_type':'percentile'
}
hoja_artistas.conditional_format(rango_celdas, formato ) 

writer.save()                
                                 
### sql ####
with sqlite3.connect('bdd_python.db') as con:
    df.to_sql('tabla',con)
    
## json 
    
df.to_json('df.json')
df.to_json('artistas_orientado_table.json',orient='table')

### ejercicios 
df_heigt = df.height 
writer =pd.ExcelWriter('colores2.xlsx',engine='xlsxwriter')
df_heigt.to_excel(writer,sheet_name="Height")
hojas_heigth = writer.sheets["Height"]

rango = 'B2:B{}'.format(len(df_heigt.index))

formato = {'type':'3_color_scale',
           'criteria': 'greater than',
           'value':     152                         
           }
hojas_heigth.conditional_format(rango,formato) 
writer.save()                                
     


# databar 

writer =pd.ExcelWriter('colores_Data_bar.xlsx',engine='xlsxwriter')
df_heigt.to_excel(writer,sheet_name="Height")
hojas_heigth = writer.sheets["Height"]

rango = 'B2:B{}'.format(len(df_heigt.index))

formato = {'type':'data_bar',
           'criteria': 'greater than',
           'value':     152                         
           }
hojas_heigth.conditional_format(rango,formato) 
writer.save()                                
#sql 
#excel 

