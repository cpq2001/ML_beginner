'''
x = int(input('请输入x：'))
t = [1,2,3,4]
try:
    print(t[x])
except:
    print('x is not a valid index')
else:
    print('noting')
finally:
    print('this is a final')
'''


'''
1.集合：集合中不含重复元素，集合中没有顺序概念，可变
2.{}表示字典而非集合，若想得到一个空集合则用set()
3.对于集合，用add(),remove()增删集合元素。min,max,len,sum函数亦可对集合操作
4.由于集合没有顺序概念，故不可以取下标访问集合元素，但可以遍历集合中的所有的元素
5.s1 | s1 ：s1并s2
6.s1 & s2 ：s1交s2
7.s1 ^ s2 ：s1对称差s2
8,s1 - s2 ：差集
'''
'''
s = {1,5,1,2,3,4}
print(s)
for x in s:
    print(x)
s1 = {5,1}
print(s1 < s) #子集，包含关系
'''

'''
1.四种容器记忆技巧：[]--list  ()--tuple {}--dict/set
2.dict = {key:value}
3.对字典条目删除仅可以用del 
4.对于字典不允许用位置访问，允许用其key访问
    4.1 对字典做遍历，for和in之间的，其实是其key
5.d.get(x,0)若有key=x则取出value，若没有key=x则增加 x：0
 
'''
d = {'one':1, 'two':2}
print(d)
print(d['two'])
d['three'] = 3
print(d)
del d['three']
print(d)
for i in d:
    print(d[i])
    print(i)
