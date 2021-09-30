
import numpy as np
import matplotlib.pyplot as plt

# 中文字体
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

#用来显示负号
plt.rcParams['axes.unicode_minus']=False

#线状图
def lineXY():
    x = np.arange(1,10)
    y =  2 * x
    plt.title("Plot XY")
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.plot(x,y)
    plt.show()

# 散点图
def ScatterXY():
    x = np.random.randn(1000)
    y = np.random.randn(1000)
    plt.title("散点图")
    plt.xlabel("x 轴")
    plt.ylabel("y 轴")
    plt.scatter(x, y, c='b')
    plt.show()

# 柱状图
def BarGragh():
    x =  [1,4,7]
    y =  [2,5,8]
    x2 =  [3,6,9]
    y2 =  [8,7,4]
    plt.bar(x, y, align =  'center')
    plt.bar(x2, y2, color =  'r', align =  'center')
    plt.title('柱状图')
    plt.ylabel('Y 坐标')
    plt.xlabel('X 坐标')
    plt.show()

# 多图并列
def TwoSubPlotGragh():

    fig = plt.figure(figsize=(10, 8), dpi=100)
    x1 = np.arange(1,10)
    y1 =  2 * x1
    plt.subplot(2,  1,  1)
    # 绘制第一个图像
    plt.plot(x1, y1)
    # plt.title('Line')
    plt.xlabel("x axis")
    plt.ylabel("y axis")

    x2 = np.arange(1,10)
    y2 =  2 * x2
    plt.subplot(2,  1,  2)
    # plt.title("散点图")
    plt.xlabel("x 轴")
    plt.ylabel("y 轴")
    plt.plot(x2,y2,'o')
    plt.show()

# 多图并列
def FourSubPlotGragh():

    fig = plt.figure(figsize=(10, 8), dpi=100)
    x1 = np.arange(1,10)
    y1 =  2 * x1
    plt.subplot(2,  2,  1)
    # 绘制第一个图像
    plt.plot(x1, y1)
    # plt.title('Line')
    plt.xlabel("x axis")
    plt.ylabel("y axis")

    x2 = np.arange(1,10)
    y2 =  2 * x2
    plt.subplot(2,  2,  2)
    # plt.title("散点图")
    plt.xlabel("x 轴")
    plt.ylabel("y 轴")
    plt.plot(x2,y2,'o')

    x3 = np.arange(1,10)
    y3 =  x3
    plt.subplot(2,  2,  3)
    # plt.title("散点图")
    plt.xlabel("x 轴")
    plt.ylabel("y 轴")
    plt.plot(x3,y3,'o')

    x4 = np.arange(1,10)
    y4 =  x4
    plt.subplot(2,  2,  4)
    # plt.title("散点图")
    plt.xlabel("x 轴")
    plt.ylabel("y 轴")
    plt.plot(x4,y4)
    plt.show()

#-----------------以下为函数测试的数据和调用部分--------------------------

lineXY()
ScatterXY()
BarGragh()
TwoSubPlotGragh()
FourSubPlotGragh()