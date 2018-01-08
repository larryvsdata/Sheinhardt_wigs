import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
import matplotlib.pyplot as plt
import datetime

df1 = pd.read_excel('THC.xlsx', sheetname='District Crime Rates & Funding')
df2 = pd.read_excel('THC.xlsx', sheetname='District Demographics')


df3=pd.merge(df1,df2,how='inner',on='District ID ')
df3=df3.sort_values(by=['District ID '],ascending=True)

million=1000000
hundredthousand=100000
colList=list(df3.columns.values)

df3[colList[1]]=df3[colList[1]]/million
df3[colList[2]]=df3[colList[2]]/hundredthousand

df3.drop(colList[0], axis=1, inplace=True)
colList=list(df3.columns.values)


df3.columns= ['CRate',
 'VCRate',
 'PoliceFunding',
 'Plus25With4YearsHSchool',
 'Year16to19NoHSchool',
 'Years18to24College',
 'Plus25With4YearsCollege']

dfCrimeRate=df3.copy()
dfCrimeRate.drop('VCRate', axis=1, inplace=True)
dfVCR=df3.copy()
dfVCR.drop('CRate', axis=1, inplace=True)





dfCrimeRate.to_csv('CrimeRate.csv', sep=',',index=False)

writer = ExcelWriter('CrimeRate.xlsx')
dfCrimeRate.to_excel(writer,'Sheet1',index=False)
writer.save()


dfVCR.to_csv('VCR.csv', sep=',',index=False)
writer = ExcelWriter('VCR.xlsx')
dfVCR.to_excel(writer,'Sheet1',index=False)
writer.save()


