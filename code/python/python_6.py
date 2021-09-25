'''
文件读写的步骤
    1.打开文件
    2.处理数据
    3.关闭文件
1.open函数：
    fileobj = open(filename, mode)
    fileobj是open()函数返回的文件对象
    mode第一个字母指明文件类型和操作的字符串，第二个字母是文件类型：
    t(可省略)文本类型，b二进制类型。
    文件打开模式：r只读(默认)，w覆盖写(不存在则新创建)
               a追加模式(不存在则创建)
2.read(size):从文件读取长度为size的字符串，若未给定或为负则读取所有内容
3.readline():读取整行返回字符串
4.readlines():读取所有行并返回列表
5.write(s):把字符串s的内容写入文件
'''
'''
#复制一个文件
fileobj1 = open("test1.txt", "r")
fileobj2 = open("test2.txt", "w")
s = fileobj1.read()
fileobj2.write(s)
fileobj1.close()
fileobj2.close()
'''

#多行文件读写
fileobj3 = open("lines.txt", "r")
for line in fileobj3.readlines():
    print(line)
fileobj3.close()