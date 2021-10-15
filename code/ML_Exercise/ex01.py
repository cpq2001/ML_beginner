import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 单变量线性回归
# 0.数据准备
path = 'ex1data1.txt'
data = pd.read_csv(path, header=None, names = ['Population','Profit'])

# 1.数据可视化
# print(data.head())
# print(data.describe())
# data.plot(kind = 'scatter', x = 'Population', y = 'Profit', figsize = (12,8))
# plt.xlabel('Profit in $10,000s')
# plt.ylabel('Population of City in 10,000s')
# plt.show()

# 2.梯度下降算法
data.insert(0, 'Ones', 1)
# 2.1 定义代价函数J
def computeCost(x,y,theta):
    # 记得将theta进行转置
    inner = np.power((x*theta.T - y),2)
    return np.sum(inner)/(2*len(x))
# 2.2 变量初始化
cols = data.shape[1]
x = data.iloc[:,0:cols-1]
y = data.iloc[:,cols-1:cols]
# print(x)
# print(type(x),type(y))
# print(y)
# print(x.values)
# print(y.values)
# 2.3 将x,y转换为numpy矩阵并计算代价函数的值
x = np.matrix(x.values)
y = np.matrix(y.values)
theta = np.matrix(np.array([0,0]))
# print('dimension of x:',x.shape,'dimension of y:',y.shape,'dimension of theta:',theta.shape)
# theta的初始值为0
# print(computeCost(x, y, theta))
# 2.4 批量梯度下降算法
# print(type(theta.shape))
# print(theta.T)
def gradientDescent(x,y,theta,alpha,iters):
    parameters = theta.ravel().shape[1]
    temp = np.matrix(np.zeros(theta.shape))
    cost  = np.zeros(iters)
    for i in range(iters):
        error = (x * theta.T) - y
        for j in range(parameters):
            term = np.multiply(error,x[:,j])
            temp[0,j] = theta[0,j] - ((alpha / len(x)) * np.sum(term))

        theta = temp
        cost[i] = computeCost(x,y,theta)
    return theta,cost
# 初始化学习速率和迭代次数
alpha = 0.01
iters = 1000
g, cost = gradientDescent(x,y,theta,alpha,iters)
# print(g)
# print(cost)
# 3.绘制线性模型以及数据
x = np.linspace(data.Population.min(), data.Population.max(), 100)
f = g[0, 0] + (g[0, 1] * x)

fig, ax = plt.subplots(figsize=(12,8))
ax.plot(x, f, 'r', label='Prediction')
ax.scatter(data.Population, data.Profit, label='Traning Data')
ax.legend(loc=2)
ax.set_xlabel('Population')
ax.set_ylabel('Profit')
ax.set_title('Predicted Profit vs. Population Size')
plt.show()