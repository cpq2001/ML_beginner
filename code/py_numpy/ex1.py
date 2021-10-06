import random

import numpy as np

t1 = np.array([1,2,3])
print(t1)
print(type(t1))
t2 = np.array(range(10))
print(t2)
t3 = np.arange(10)
print("t3",t3)
print(t3.dtype)
t4 = np.array([1,0,1,0], dtype=bool)
print(t4)
#numpy中的小数
t5 = np.array([random.random() for i in range(10)])
print(t5)
t6 = np.round(t5,2)
print(t6)
t7 = np.array([[1,2],[1,2],[1,3]])
print(t7.shape)
#获取长度：t7.shape[0]*t7.shape[1]
print(t7)
t8 = t3.reshape((2,5)) #t3本身不会变化
print(t8)
t9 = t8.flatten()
print(t9)