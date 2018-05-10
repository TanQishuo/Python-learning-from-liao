# -*- coding: utf-8 -*-
"""
Created on Wed May  9 22:07:03 2018

@author: 123456
"""

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
from functools import reduce
   
def findTimes(s):
    if len(s) == 0:
        return 0
    else:
        for i in range(len(s)):
            if s[i] == '.':
                return len(s)-1-i
        return 0
def removePoint(s):
    if len(s) == 0:
        return s
    else:
        for i in range(len(s)):
            if s[i] == '.':
                return s[:i] + s[i+1:]
        return s

digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,'9':9}
def str2float(s):
    b = findTimes(s)
    ss = removePoint(s)
    def str2int(s):
        def fn(x,y):
            return x*10 + y
        def char2num(s):
            return digits[s]
        return reduce(fn,map(char2num,s))
    
    return str2int(ss)/ 10 ** b


# 测试
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
