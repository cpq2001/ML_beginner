import matplotlib.pyplot as plt
import random
font = {'family' : 'MicroSoft YaHei',
        'weight' : 'bold'
        }
plt.rc('font', **font)

#绘制直方图
a = random.sample(range(80,151),70)
#计算组数
d = 5
num_bins = (max(a) - min(a))//d
plt.hist(a,num_bins,density=True)
plt.xticks(range(min(a),max(a)+d,d))
plt.grid()
plt.show()

