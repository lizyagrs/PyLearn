import numpy as np
vector = np.array([1, 2, 3, 4])
metrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

result=np.where(metrix < 5, 0, metrix)
result=np.where(result >= 5, 1, result)
print(result)
result2=np.where(metrix >= 5, 1, 0)
print(result2)
