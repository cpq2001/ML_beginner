import numpy as np
# 练习：data1 和 data2 的数据分别编号0，1后再拼接再一起
d_1 = "./data1.txt"
d_2 = "./data2.txt"
d_1 = np.loadtxt(d_1,delimiter=',',dtype=int)
d_2 = np.loadtxt(d_2,delimiter=',',dtype=int)
zeros = np.zeros((d_1.shape[0],1)).astype(int) #创建一个全0的数组
ones = np.ones((d_2.shape[0],1)).astype(int)
d_1 = np.hstack((zeros,d_1))
d_2 = np.hstack((ones,d_2))
d = np.vstack((d_1,d_2))
print(d)

