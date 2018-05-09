# -*- coding: utf-8 -*-
"""
Created on Wed May  9 13:29:10 2018

@author: 123456
"""

from functools import reduce

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
def normalize(name):
    if len(name) == 0:
        return print("未输入名字")
    else:
        name2 = ['']
        if not 'a' <= name[0] <= 'z':
            name2.append(name[0])
        else:
            i = ord(name[0])
            i = i - 32
            name2.append(chr(i))
        for n in name[1:]:
            if not 'A' <= n <= 'Z':
                name2.append(n)
            else:
                i = ord(n)
                i = i + 32
                name2.append(chr(i))
        return ''.join(name2)

# 测试:
L1 = ['adam', 'LISA', 'barTg','FEWFGdfdfGFSAGREWGTEtgergafdasGFdgAGAVA','']
L2 = list(map(normalize, L1))
print(L2)

    
