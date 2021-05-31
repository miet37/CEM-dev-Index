# -*- coding: utf-8 -*-
"""
Created on Wed May 19 20:07:53 2021

@author: user
"""
import pandas as pd
from sklearn import preprocessing
import numpy as np
#import matplotlib.pyplot as plt

#read data
df1 = pd.read_excel("cei_zbiorczo.xlsx", sheet_name="Sheet1")
#df1.to_excel("df1.xlsx")
#datasets
dfg = df1.groupby("data_set").count().reset_index()
#dfg.to_excel("dfg.xlsx")

print(df1.shape)
print(df1.sample(3)    )
print(df1.columns)
print(df1.index)

cols=[x for x in range(2008,2020)]

#fillna by interpolation
#for y in cols:
df2 = df1[cols].apply(pd.to_numeric).interpolate(axis=1)
df2a = df1.join(df2,rsuffix="x")
df2a.columns
#df2a.to_excel("df2a.xlsx")

df3 = df2+1
df4 = np.log10(df3)

df4.columns = df4.columns.map(lambda x: str(x) + 'log')
df5 = df2a.join(df4)
df5.columns
#df5.to_excel("df4a.xlsx")

colsx = [str(x)+"log" for x in cols]

#trend detection
aa = []
for s in dfg["data_set"]:
    a=[]
    b=[]
    dfi = df5[df5.data_set==s][colsx]
    for i in range(0,dfi.shape[0]):
        a.append(np.polyfit(cols,dfi.iloc[i],1)[0])
        sp = dfi.iloc[i][0]
        ds = 0
        for t in dfi.iloc[i][1:]:
            ds += t-sp
            sp = t 
        b.append(ds) 
    p=(round(len([x for x in a if x>0])/len(a),2))
    p1=(round(len([x for x in b if x>0])/len(b),2))
#    print(p,', ',p1)
    aa.append([s,p,p1])
#    print(aa)

dfg['Pos_trend'] = aa
#dfg.to_excel("dfg_ternds.xlsx")

a = []
b = []
for y in colsx:
    #pivoting 
    print(y)
    dfx = df5.pivot(index='geo',columns='data_set',values=y)

    # fillna mean
    cols1 = [x for x in dfx.columns]
    for x in cols1:
        dfx[x].fillna(value=dfx[x].mean(),inplace=True)

    dfx['Year'] = y[0:4]
    a.append(dfx)
    
    #normalization
    
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(dfx[cols1])
    df6 = pd.DataFrame(data=x_scaled, columns=cols1).round(2)

    df6['geo'] = dfx.index       
    df6['Sum'] = df6.sum(axis=1)
    df6['pct_rank'] = df6['Sum'].rank(pct=True)
    df6.set_index('geo', inplace=True)
    
    dfxx = dfx.join(df6.round(2), lsuffix="_fna_mean")
    b.append(dfxx)

dfx1 = pd.concat(a)
dfx2 = pd.concat(b)

# ...
writer = pd.ExcelWriter('dfxx3.xlsx')

dfx2.to_excel(writer, sheet_name="dfx_norm")
df5.to_excel(writer, sheet_name="Org_log")
dfg.to_excel(writer, "dfg_ternds.xlsx")

writer.save()








'''
tx = [
      [4,5,6,7,8,9,10,22,22,34],
      [2,3,4,5,6,7,8,9,10,20],
      [10,20,30,40,50,60,70,80,90,100],
      [20,30,40,50,60,70,80,90,100,200]
      ]
mm_scaler = preprocessing.MinMaxScaler()
tx_scaled = min_max_scaler.fit_transform(tx)
dft = pd.DataFrame(data=tx_scaled).round(2)
dft


x = df1[cols].values #returns a numpy array
st_scaler = preprocessing.StandardScaler()
x_scaled = st_scaler.fit_transform(x)
df1x = pd.DataFrame(x_scaled)


#from sklearn.linear_model import LinearRegression
#model = LinearRegression()
#model.fit(cols, dfi.iloc[0])
# calculate trend
#trend = model.predict(x)

def trenddetector(list_of_index, array_of_data, order=1):
    result = np.polyfit(list_of_index, list(array_of_data), order)
    slope = result[-2]
    return float(slope)

print(trenddetector(x,y))


#datasets_years
for ds in dfg["data_set"]:
    cols=[x for x in range(2008,2019)]



'''