# -*- coding: utf-8 -*-
"""
Created on Fri May 11 13:43:28 2018

@author: 123456
"""

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
        
def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)
        

for n in primes():
    if n < 1000:
        print(n)
    else:
        break
    
print("===============================================")
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    s = str(n)
    l = len(s)
    if l == 0:
        return False
    if l == 1:
        return True
    else:
        m = l // 2
        for i in range(m):
            return s[i] == s[l-1-i]
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
