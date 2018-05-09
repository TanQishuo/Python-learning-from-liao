# -*- coding: utf-8 -*-
"""
Created on Wed May  9 08:46:13 2018

@author: 123456
"""
#Iteration
def findMinAndMax(L):
    if len(L) == 0:
        Max = None
        Min = None
        return (Max,Min)
    else:
        Max = L[0]
        Min = L[0]
        for i in range(len(L)):
            if Max <= L[i]:
                Max = L[i]
            if Min >= L[i]:
                Min = L[i]
        return (Min,Max)
    
print(findMinAndMax([]))
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')