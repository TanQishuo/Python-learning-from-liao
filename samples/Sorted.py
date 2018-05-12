# -*- coding: utf-8 -*-
"""
Created on Sat May 12 21:51:44 2018

@author: tanqishuo
"""

#假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(len(L))
#请用sorted()对上述列表分别按名字排序：
def by_name(t):
    return t[0]
print(by_name(L))
#测试
L2 = sorted(L, key=by_name)
print(L2)
print("==================================================")
    
#再按成绩从高到低排序：
def by_score(t):
    return t[1]

print(by_score(L))
#测试
L3 = sorted(L, key=by_score, reverse=True)
print(L3)