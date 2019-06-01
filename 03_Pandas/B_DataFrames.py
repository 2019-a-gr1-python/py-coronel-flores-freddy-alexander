# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:39:32 2019

@author: alex
"""

import numpy as np
import pandas as pd 

arr_rand = np.random.randint(0,10,6).reshape(2,3)

df = pd.DataFrame(
        arr_rand,
        columns =['Estatura','Peso','Edad']
    )


df2 = pd.DataFrame(
        arr_rand
        
    )
    
df2.columns = ['Estatura','Peso','Edad']
df2.index = ['Alex','Adrian']
df2
df3 = pd.DataFrame(
        arr_rand
        
    )


df3[0]

df2['Estatura'][0]

df4 = pd.DataFrame(
        arr_rand,
        columns =['Estatura','Peso','Edad'],
        index = ['Alex','Adrian']
        
    )
    
df4['Estatura']['Alex']
df4['Peso']['Adrian']







