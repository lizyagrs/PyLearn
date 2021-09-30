# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename="Meteo_Wuhan.csv"

df=pd.read_csv(filename, index_col=0, parse_dates=True)

print("表格行列数:\n{0}".format(df.shape))#行列数

print("获取到全部值:\n{0}".format(df))#格式化输出

data=df.iloc[0:10,0:6]
print("读取指定行的数据：\n{0}".format(data))#格式化输出

data=df.iloc[11:19,1:5]
print("读取指定行列的数据：\n{0}".format(data))#格式化输出

# fig = plt.figure()
df.plot(style="-o", figsize=(12, 6))
plt.show()

data = df.values
print("输出列标题:\n{0}".format(df.columns.values))
# print(data)#格式化输出

allcolomn_mean=data.mean(axis = 0)# 计算所有列的平均值
print("获取所有列的平均值:\n{0}".format(allcolomn_mean))