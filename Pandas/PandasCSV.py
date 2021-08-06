# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

filename='Meteo_Wuhan.csv' #"Meteo_Wuhan.csv"

df=pd.read_csv(filename)

data = df.head()

print("获取到前5行的值:\n{0}".format(data))#格式化输出