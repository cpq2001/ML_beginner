'''
容器分为：1.序列容器 2.非序列容器
其中，序列容器有字符串、列表
非序列容器有集合
1.切片操作：对字符串的切片操作后还是字符串，对列表切片还是列表
    1.1 巧用[0:-1]可以取出第一个到倒数第二个的序列
    1.2 [3:]表示从3取到最后一个
2.len,min,max等函数都可以作用于序列
3.字符串函数，使用时：字符串.函数名
    3.1 .lower()
    3.2 .find() 找不到返回-1
    3.3 .count()
    3.4 .strip() 去掉两边空格
        3.4.1 若想只去除左边空格 .lstrip()  右边.rstrip()
    3.5 .replace('a', 'b') 把字符串中的a替换为b
4.所有的字符串函数都不会修改该字符串本身，而是在该字符串做修改后产生一个新的字符串
5.str()可以将括号内的内容转换为字符串

'''

'''
s = 'CPQQPC'
s1 = s.lower()
print(s1)
print(s.find('Q'))
print(s.count('C'))
s2 = s.replace('Q','q')
print(s2)

'''

'''
1.列表中的元素可以是不同的类型
2.list()可以将字符串转成列表
'''
'''
a = 1
b = 3
t = [a, b - 2]
print(t)
s = 'this is a boy'
t1 = list(s)
print(t1)

t2 = [[1,2],[1,2,3],[0,1]]
print(len(t2))
print(t2[1])
del t2[1] #删除某一个元素
print(t2)
'''
'''
1.列表的函数
    1.1 .append()
    1.2 .extend()
    1.3 .insert()
    1.4 .remove()
    1.5 .pop()
    1.6 .reverse()
    1.7 .index()
'''
'''
t = [0,1,2,3]
print(t)
t.append(4)
print(t)
t.append([0,1])
print(t)
t.extend([1,2])
print(t)
t.insert(1,9)
print(t)
t.remove(0)
print(t)
t.pop(3)
print(t)
t.reverse()
print(t)
x = t.index(1)
print('索引为：', x)

'''


# s = 'this is a test.'
# t1 = s.split()
# print(t1)
# t2 = list(s)
# print(t2)
# ss = '12::32'
# tt1 = ss.split('::')
# print(tt1)
# tt2 = ss.split(':')
# print(tt2)
# st = ' '.join(t1)
# print(st)


'''
1.元组(tuple)是一种不可修改的数据类型这和list不一样
    p = (1,2,3)
    p[0] = 4 #错误！
2.所有可能会修改元组的函数都不能作用于元组
3.一些数据放在一起中间用逗号，隔开并且外面没有括号，则py默认其外面有元组的圆括号（）

'''
'''
t = 'test1'
p = tuple(t)
print(p)
p1 = (1, '1')
print(p1)
'''


import random
t = [1,2,5,9,8,4,7,1]
t.sort()
print(t)
random.shuffle(t)
print(t)
x = random.choice(t)
print(x)
y = random.random()
z = random.randint(80,151)
print(y,z)
q = random.sample(range(80,151),10)
print(q)

