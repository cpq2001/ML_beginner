import  numpy as np
t1 = np.array(range(10))
t2 = t1.reshape((2,5))
print(t2)
t3 = t2 + 2
print(t3)
#转置
t4 = t3.T
print(t4)