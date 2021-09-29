import matplotlib.pyplot as plt
font = {'family' : 'MicroSoft YaHei',
        'weight' : 'bold'
        }
plt.rc('font', **font)

y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,12]
x_3 = range(1,31)
x_10 = range(51,81)
plt.figure(figsize=(15,10),dpi=100)
plt.scatter(x_3,y_3,label='3月')
plt.scatter(x_10,y_10,label='10月')
#调整x轴刻度
_x = list(x_3) + list(x_10)
_x_labels = ["3月{}日".format(i) for i in x_3]
_x_labels += ["10月{}日".format(i) for i in x_3]
plt.xticks(_x[::3],_x_labels[::3],rotation=45)
plt.legend()
plt.xlabel("日期")
plt.ylabel("温度")
plt.title("3月份和10月份气温变化情况")
plt.show()