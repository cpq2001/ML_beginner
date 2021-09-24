'''
1.整数不同进制表示：
            前导符     示例
    二进制   0b或0B     0b10
    八进制   0o或0O     0o10
    十六进制 0x或0X     0x10
2.浮点数运算存在不确定尾数，有误差，可以用round()函数解决
3.复数（complex）类型：其他语言不具有的
    3.1 虚部用j表示
    3.2 例如2 + 3j
    3.3 real 方法取实部   imag 方法取虚部
    3.4 complex()函数可用于创建一个值为real + imag*j的复数
4.除法运算：和其他语言不一样
    4.1: /:浮点数除法
    4.2: //:整数除法(向数轴取整)
5.求余运算：python也可以作用于浮点数
6.求幂运算：2**3 = 8
'''
'''
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3) #False
print(round(0.1 + 0.2, 2) == 0.3) #True
c = complex(2, 3)
print(c)
'''

'''
1.python中所有字符都以字符串形式存在
2.表示形式可以是: 单引号 双引号 三引号
    2.1 其中三引号可以表示多行文本
    2.2 若字符串中有单引号我们则可以用双引号，反之亦可（当然可以用转义符）
    2.3 若字符串单双引号都有，则三引号就可以发挥作用了
3.字符串运算符
    3.1 运算符+：连接字符串(字符串只可以和字符串相加)
    3.2 运算符*：复制字符串
4.字符串切片
    0  1  2  3  4
    a  b  c  d  e
   -5 -4 -3 -2 -1
    4.1 切片：在[]中给出切片序号范围(左闭右开区间)
5.逻辑运算和关系运算的结果是布尔值
'''
'''
print('xyz' * 3)
s = 'abcde'
print(s[1:4])
'''

'''
1.所谓内置函数就是不需要导入库可以直接使用
2.bin():将整数转换成2进制字符串    
  oct()：将整数转换成8进制字符串
  hex()：将整数转换成8进制字符串
3.str():创建一个字符串
  list():根据传入的参数创建一个新列表
    3.1 str(123)   >>>   '123
    3.2 list('abc')   >>>   ['a','b','c']
4.int(x[,base=10])
5.ord()和chr()
    5.1 ord('a'):ASCII码97
    5.2 ord('中'):汉字'中'的Unicode码
    5.3 chr(97):参数类型为整数，返回'a'
'''
'''
x = 5
print(bin(x))
print(oct(x))
print(hex(x))
print(type(bin(x)))
t = int('35', 8)
print(type(t))
print(t)
'''

'''
1.x, y = 4, 8 #x=4,y=8
  x, y = "ab" #x='a' y='b'
2.在python中想交换两数的值只需要：x,y=y,x
3.i,*j=[1,2,3] #i=1 j=[2,3]
'''

'''
1.for语句
    for variable in 列表：
2.range(start,stop,step)
    start: 默认是0
        如range(5)等价于range(0,5)
    stop:到stop结束但不包括stop
    step:步长，默认是1
        如range(0，5)等价于range(0,5,1)
'''
'''
#产生一个0~9的列表
l = list(range(10))
print(l)
#产生一个从0到-9的递减的列表
ll = list(range(0, -10, -1))
print(ll)
#计算1+2+...+n
n = int(input())
res = sum(list(range(1, n+1)))
print(res)
'''

'''
1.列表支持加法、乘法、比较、索引、切片操作等等
2.列表推导式（又列表解析式）提供了一种简明扼要的方法来创建列表
    基本格式：[expression for item in iterable]
'''
'''
n = [2 * num for num in [1,2,3]]
print(n)
nl = [num for num in range(1, 8) if num % 2 == 1]
print(nl)
'''

'''
1.format()
    基本格式：str.format()
    print("{0:.2f} {1:.2f}".format(x, y))
    0和1表示format函数中的第一个和第二个参数
    .2f四舍五入保留2位小数
'''
x = 3.14159
y = 2 * 3
print("{0:.2f} {1:.2f}".format(x, y))