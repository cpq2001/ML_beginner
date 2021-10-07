import numpy as np
# #创建一个对角线为1的方阵
# f = np.eye(3).astype(int)
# print(f)
# 获取最大，小值的位置
# print(np.argmax(d,axis=0))
# print(np.argmax(d,axis=1))

# # 随机函数
np.random.seed(10)
t = np.random.randint(10,20,(4,5)).astype("float32")
print(t)
# # a = b[:]  视图的操作，a的数据完全由b保管
# # a = b.copy a,b互补影响

# numpy.nan
# 1. np.nan != np.nan ,利用这一特性可以判断nan的个数
# 2. nan和任何数相加都是nan
t[0,0] = np.nan
print(np.count_nonzero(t))
print(t)
print(np.count_nonzero(t!=t))
tt = t[:,0]
print(tt)
ttt = tt[tt==tt]
print(ttt)
