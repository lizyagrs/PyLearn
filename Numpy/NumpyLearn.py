import numpy as np

'''
数学
'''
# a = np.array([1, 2, 3])
# print(a)
a = np.array([1, 2, 3, 4, 5, 6])
print(a)
b = a[4]
print("数组a中的第5项是: %d" % b)

'''
矩阵与矩阵运算
'''
print('矩阵a：')
metrix_a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(metrix_a)
# print(metrix_a.shape)

print('矩阵b：')
metrix_b = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]])
print(metrix_b)

print('矩阵c：')
metrix_c = metrix_a + metrix_b
print(metrix_c)

'''
统计函数
'''

max_a = np.amax(metrix_a)
print(metrix_a)
print("metrix_a的最大值是: %d" % max_a)

min_c = np.amin(metrix_c)
print(metrix_c)
print("metrix_c的最小值是: %d" % min_c)