# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

# filename='Meteo_Wuhan.xlsx'
# df=pd.read_excel(filename)
filename="Meteo_Wuhan.csv"

df=pd.read_csv(filename)

print("表格行列数:\n{0}".format(df.shape))#行列数

data_head = df.head(10)
print("获取到前10行的值:\n{0}".format(data_head))#格式化输出

data = df.values
print("输出列标题:\n{0}".format(df.columns.values))
print(data)#格式化输出