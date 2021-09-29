import matplotlib.pyplot as plt
font = {'family' : 'MicroSoft YaHei',
        'weight' : 'bold'
        }
plt.rc('font', **font)
#绘制横着的条形图
a = ['战狼2','速激2','变形金刚5','摔跤吧爸爸']
b = [56.01,26.94,44.9,39.2]
x = len(a)
plt.figure(figsize=(15,10),dpi=100)
plt.barh(a,b,height=0.3)
plt.savefig("../imag/piaofang.png")