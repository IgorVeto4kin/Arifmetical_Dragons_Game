import numpy as np
# 1
a = np.arange(12,43,1)
#2
a = np.full((12,1), 0)
a[4] = 1
#3
a = np.array([[0, 1, 2], [3, 4, 5], [6,7,8]])
#4
positive_martix = a[a > 0]
#5
a = np.array([[0, 1, 4], [3,4,5],[9,8,7],[7,6,5],[1,5,7]])
b = np.array([[4,5],[8,9],[2,5]])
rez = np.dot(a, b)
#6
d = np.full((10,10), 1)
d[0, :], d[9, :], d[:, 0], d[:, 9],  = [0]*10, [0]*10, [0]*10, [0]*10
#7
e = np.random.random((7,))
e = sorted(e)
#8
a = np.arange(9).reshape(3,3)
for index, value in np.ndenumerate(a): print(index, value)