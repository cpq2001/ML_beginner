import matplotlib.pyplot as plt
import  random
# x = range(2, 7, 2)
# y = [1, 2, 7]
# # 设置图片大小,dpi:dot per image
# fig = plt.figure(figsize=(20,15), dpi=(100))
#
# # 绘图
# plt.plot(x, y)
#
# # 绘制x轴的刻度,y轴同理
# _xtick_l = [(i + 0.5) for i in range(2,7,2)]
# plt.xticks(_xtick_l)
#
# # 保存，在绘图后进行
# # plt.savefig("./p1.svg")
#
# # 展示图形
# plt.show()

# 练习：绘制10~12点的气温
# 设置中文字体，matplotlib默认不显示中文
font = {'family' : 'MicroSoft YaHei',
        'weight' : 'bold'
        }
plt.rc('font', **font)

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]
plt.figure(figsize=(20,15), dpi=100)
plt.plot(x, y)
# 调整x轴的刻度,需要先绘图
_xtick_lables = ["10点{}分".format(i) for i in range(60)]
_xtick_lables += ["11点{}分".format(i) for i in range(60)]
plt.xticks(x[::3], _xtick_lables[::3], rotation = 45)
#添加描述信息
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("10时-12时的气温变化情况")
plt.savefig("../imag/tem4.png")
