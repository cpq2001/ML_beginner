import numpy as np
# #创建一个对角线为1的方阵
# f = np.eye(3).astype(int)
# print(f)
# 获取最大，小值的位置
# print(np.argmax(d,axis=0))
# print(np.argmax(d,axis=1))

# 随机函数
t = np.random.randint(10,20,(4,5))
print(t)

# a = b[:]  视图的操作，a的数据完全由b保管
# a = b.copy a,b互补影响