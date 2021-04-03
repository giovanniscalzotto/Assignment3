# 1 importing data

import pandas as pd
import numpy as np
import csv

ff = pd.read_csv('HTML_Scapper_FForner.csv')
gs = pd.read_csv('hw2.csv')
ag = pd.read_csv('companies_list.csv')
kk = pd.read_csv('Webscraper.csv')

ff.drop(ff.columns[[0]], axis=1, inplace=True)
ag.drop(ag.columns[[0]], axis=1, inplace=True)
kk.drop(kk.columns[[0]], axis=1, inplace=True)
ff.columns = ['Name', 'Purpose']
ag.columns = ['Name', 'Purpose']
kk.columns = ['Name', 'Purpose']

df_final =  gs.append(ff).append(ag).append(kk)
df_final[''] = [i for i in range(200)]
df_final.set_index([''], inplace = True, append = False, drop = True) 
print(df_final)


# 2
#df_final.to_csv('df_final.csv') 










