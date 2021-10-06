import  numpy as np
file_path = "./data1.txt"
t1 = np.loadtxt(file_path,delimiter=",",dtype="int")
print(t1)
print("*"*100)
# #取连续的多行
# print(t1[3:])
# #取不连续的多行
# print(t1[[2,4,6]])
# #取连续的列
# print(t1[:,2:])
# #取不连续的多列
# print(t1[:,[0,3]])
# #取第三行第二列
# print(t1[3,2])
# #取多行多列
# print(t1[2:5,0:2])
# #取多个不相邻的点(选出来的点:（0，2），（1，3），（3,0）)
# print(t1[[0,1,3],[2,3,0]])

# t2 = t1<40
# print(t2)
# t1[t1<40] = 40
# print(t1)
# t2 = np.where(t1>=40,50,60)
# print(t2)
t3 = t1.clip(40,50)
print(t3)