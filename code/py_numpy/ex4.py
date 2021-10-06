import  numpy as np
# t1 = np.array(range(10))
# t3 = np.array(range(10,20))
# t2 = t1.reshape((2,5))
# t4 = t3.reshape((2,5))
# print(t2)
# print(t4)
# # 数组的拼接
# tt1 = np.vstack((t2,t4))
# tt2 = np.hstack((t2,t4))
# print(tt1)
# print(tt2)

# 行、列交换
t = np.arange(12,24).reshape(3,4)
print(t)
t[[1,2],:] = t[[2,1],:] # 行交换
print(t)
t[:,[0,2]] = t[:,[2,0]] # 列交换
print(t)