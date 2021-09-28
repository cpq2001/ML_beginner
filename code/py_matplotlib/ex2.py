import matplotlib.pyplot as plt
font = {'family' : 'MicroSoft YaHei',
        'weight' : 'bold'
        }
plt.rc('font', **font)
# 动手1
# y = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
# x = range(11,31)
# plt.figure(figsize=(20,15),dpi=100)
# plt.plot(x,y)
# _xticks_labels = ["{}岁".format(i) for i in x]
# plt.xticks(x,_xticks_labels)
# #绘制网格
# plt.grid()
# plt.show()

# 动手2
y1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y2 = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]
x = range(11,31)
plt.figure(figsize=(20,15),dpi=100)
plt.plot(x,y1,color='orange',label='自己')
plt.plot(x,y2,color='cyan',label='同桌')
_xticks_labels = ["{}岁".format(i) for i in x]
plt.xticks(x,_xticks_labels)
#绘制网格
plt.grid()
plt.legend()
plt.show()