import matplotlib.pyplot as plt
# 中文字体
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
# family='Times New Roman',

x = [[1, 2,3], [3, 4,5]]  # [1,3]是线段1两端点的x坐标
y = [[3, 3,3], [3, 3,3]]  # [1,3]是线段1两端点的y坐标
plt.figure()  # 创建绘制窗口

for i in range(len(x)):
    plt.plot(x[i], y[i], color='g')
    plt.scatter(x[i], y[i], color='y')
    # ax.text(430, 337, "北京", fontsize=12, color = "r", style = "italic", weight = "light", verticalalignment='center', horizontalalignment='right', rotation=90)
plt.text(1,3,"1号\n10吨",fontsize=12, weight = "light",verticalalignment='bottom',horizontalalignment='center')
plt.text(2,3,"2号\n20吨",fontsize=12, weight = "light",verticalalignment='bottom',horizontalalignment='center')
plt.text(3,3,"3号\n空",fontsize=12, weight = "light",verticalalignment='bottom',horizontalalignment='center')
plt.text(4,3,"4号\n空",fontsize=12, weight = "light",verticalalignment='bottom',horizontalalignment='center')
plt.text(5,3,"5号\n40吨",fontsize=12, weight = "light",verticalalignment='bottom',horizontalalignment='center')
plt.show()