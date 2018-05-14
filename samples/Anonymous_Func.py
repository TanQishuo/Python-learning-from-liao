# -*- coding: utf-8 -*-
"""
Created on Mon May 14 22:04:22 2018

@author: 123456
"""

#请用匿名函数改造下面的代码：
'''def is_odd(n):
    return n % 2 == 1
'''
L = list(filter(lambda x : x % 2 == 1, range(1, 20)))
print(L)