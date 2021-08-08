# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename="Meteo_Wuhan.csv"

df=pd.read_csv(filename, index_col=0, parse_dates=True)

print("表格行列数:\n{0}".format(df.shape))#行列数

data_head = df.head(31)
print("获取到前31行的值:\n{0}".format(data_head))#格式化输出

# fig = plt.figure()
df.plot(style="-o", figsize=(12, 6))
plt.show()
data = df.values
print("输出列标题:\n{0}".format(df.columns.values))
# print(data)#格式化输出

allcolomn_mean=data.mean(axis = 0)# 计算所有列的平均值
print("获取所有列的平均值:\n{0}".format(allcolomn_mean))