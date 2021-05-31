# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:59:11 2021

@author: mieczysław pawłowski
"""
import pandas as pd
import eurostat

dane_to_load = pd.read_excel("ce_mp_v4.xlsx", sheet_name="Dane")
print(dane_to_load)

for n, fi in dane_to_load.iterrows():
    print(fi.data_set)
    dftab = eurostat.get_data_df(fi.data_set)
    excel_file_name = fi.data_set + ".xlsx"
    dftab['data_set']=fi.data_set
    dftab['data_name']=fi.data_name
    for c in dftab.columns[0:-1]:
        if type(c)==int and c>1990 and c < 2008:
            dftab.drop(c, inplace=True, axis=1)
            print('dropped ', c)
           
    dftab.to_excel(excel_file_name)
    
    
'''
    
't2020_rt200'
'env_ac_rme'
  
'''
  
def ds(data_set):
    dftab = eurostat.get_data_df(data_set)
    print(dftab.shape)
    print(dftab.sample(3)    )
    print(dftab.columns)
    print(dftab.index)

ds('env_wasgen')

##########
#weee collection by househelds
fi = 'env_waselee'
dftab = eurostat.get_data_df(fi)
print(dftab.shape)
print(dftab.sample(3)    )
print(dftab.columns)
print(dftab.index)
dftab = dftab[dftab['wst_oper']=='COL_HH']
dftab = dftab[dftab['unit']=='KG_HAB']
dftab = dftab[dftab['waste']=='TOTAL']
excel_file_name = fi+'.xlsx'
dftab['data_set']=fi
#dftab['data_name']=fi.data_name
for c in dftab.columns[0:-1]:
    if type(c)==int and c>1900 and c < 2008:
        dftab.drop(c, inplace=True, axis=1)
        print('dropped ', c)

dftab.to_excel(excel_file_name)

########
#energy consumtion
fi = 'sdg_07_20'
dftab = eurostat.get_data_df(fi)
print(dftab.shape)
print(dftab.sample(3)    )
print(dftab.columns)
print(dftab.index)
#dftab = dftab[dftab['wst_oper']=='COL_HH']
#dftab = dftab[dftab['unit']=='KG_HAB']
#dftab = dftab[dftab['waste']=='TOTAL']
excel_file_name = fi+'.xlsx'
dftab['data_set']=fi
#dftab['data_name']=fi.data_name
for c in dftab.columns[0:-1]:
    if type(c)==int and c>1900 and c < 2008:
        dftab.drop(c, inplace=True, axis=1)
        print('dropped ', c)

dftab.to_excel(excel_file_name)

########
#energy consumtion
fi = 'sdg_07_20'
dftab = eurostat.get_data_df(fi)
print(dftab.shape)
print(dftab.sample(3)    )
print(dftab.columns)
print(dftab.index)
#dftab = dftab[dftab['wst_oper']=='COL_HH']
#dftab = dftab[dftab['unit']=='KG_HAB']
#dftab = dftab[dftab['waste']=='TOTAL']
excel_file_name = fi+'.xlsx'
dftab['data_set']=fi
#dftab['data_name']=fi.data_name
for c in dftab.columns[0:-1]:
    if type(c)==int and c>1900 and c < 2008:
        dftab.drop(c, inplace=True, axis=1)
        print('dropped ', c)

dftab.to_excel(excel_file_name)


########
#Wather consumption
ENV_WAT_CAT

fi = 'env_wat_cat'
dftab = eurostat.get_data_df(fi)
print(dftab.shape)
print(dftab.sample(3)    )
print(dftab.columns)
print(dftab.index)
#dftab = dftab[dftab['wst_oper']=='COL_HH']
#dftab = dftab[dftab['unit']=='KG_HAB']
#dftab = dftab[dftab['waste']=='TOTAL']
excel_file_name = fi+'.xlsx'
dftab['data_set']=fi
#dftab['data_name']=fi.data_name
for c in dftab.columns[0:-1]:
    if type(c)==int and c>1900 and c < 2008:
        dftab.drop(c, inplace=True, axis=1)
        print('dropped ', c)

dftab.to_excel(excel_file_name)


########
#Wather consumption
ENV_WAT_CAT

fi = 'repair_ee_hh'
dftab = eurostat.get_data_df(fi)
print(dftab.shape)
print(dftab.sample(3)    )
print(dftab.columns)
print(dftab.index)
#dftab = dftab[dftab['wst_oper']=='COL_HH']
#dftab = dftab[dftab['unit']=='KG_HAB']
#dftab = dftab[dftab['waste']=='TOTAL']
excel_file_name = fi+'.xlsx'
dftab['data_set']=fi
#dftab['data_name']=fi.data_name
for c in dftab.columns[0:-1]:
    if type(c)==int and c>1900 and c < 2008:
        dftab.drop(c, inplace=True, axis=1)
        print('dropped ', c)

dftab.to_excel(excel_file_name)







import matplotlib.pyplot as plt

fig, ax = plt.subplots()
x=dftab.columns[2:]

for i in dftab.index:
    ax.plot(x,dftab.iloc[i][2:])


dane_to_load = pd.read_excel("Ce_index2_dane_to_load.xlsx", sheet_name="Dane")
print(dane_to_load)

for n, fi in dane_to_load.iterrows():
    print(fi.data_set)
    dftab = eurostat.get_data_df(fi.data_set)
    excel_file_name = fi.data_set + ".xlsx"
    dftab['data_set']=fi.data_set
    dftab['data_name']=fi.data_name
    for c in dftab.columns[0:-1]:
        if type(c)==int and c>1990 and c < 2008:
            dftab.drop(c, inplace=True, axis=1)
            print('dropped ', c)
           
    dftab.to_excel(excel_file_name)






