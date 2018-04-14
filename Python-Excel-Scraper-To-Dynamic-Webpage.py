# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 23:27:08 2018

@author: Brajesh
"""

# using the ExcelFile class
import pandas as pd
#data = {}
#with pd.ExcelFile('ABN_POD1_RVTools_20180319.xls') as xls:
#    data['Sheet1'] = read_excel(xls, 'Sheet1', index_col=None, na_values=['NA'])
#    data['Sheet2'] = read_excel(xls, 'Sheet2', index_col=None, na_values=['NA'])

# equivalent using the read_excel function
#data = read_excel('path_to_file.xls', ['Sheet1', 'Sheet2'], index_col=None, na_values=['NA'])

xl = pd.ExcelFile("SAMPLE1.xlsx")
print(xl.sheet_names)
df1 = xl.parse("vInfo", header=0)
df2 = xl.parse("vDatastore", header=0)
#print(df)
#df1[df1['VM'] == 'i01-lr65-64-20170503']
df1=df1[df1['Host'].str.contains('nl03esx141ccpv1')]
df2=df2[df2['Name'].str.contains('bb2')]
#print(df.to_html('html14apr2018.html'))
#df.filter(items=['Powerstate'])
#df_filtered = df1.query('salary>30000')
#df1 = df1.query('#VMs>10')
#df1 = df1[[[0],[1],[2]]
print(df1['Host'])
print(df2['Name'])
df1.to_html('html14apr2018vInfo.html')
df2.to_html('html14apr2018vDatastore.html')
