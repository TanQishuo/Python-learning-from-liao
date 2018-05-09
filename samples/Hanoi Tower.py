# -*- coding: utf-8 -*-
"""
Created on Tue May  8 11:24:12 2018

@author: 123456
"""

# Hanoi Tower question



Hanoi(5,'A','B','C')

#构造Hanoi函数，目的是将n个物体从sub1移到sub3，任何过程大小顺序不能变
#sub2为辅助，需要的时候使用
def Hanoi(n,sub1,sub2,sub3):
    i = 0
    if(n == 1):
        move(sub1,sub3) #当n=1时，只做一件事，就是把sub1上的它移到sub3上
        i = i + 1
    # n>1时，令n-1的物体移动
    else:
        Hanoi(n-1,sub1,sub3,sub2) #将n-1物体借助sub3移到sub2上
        move(sub1,sub3) #将n从sub1移到sub3上
        Hanoi(n-1,sub2,sub1,sub3) #将n-1物体借助sub1移到sub3上
        i = i + 3
    return print("总共移动了%d次" %i)

def move(x,y):
    print("%s -> %s" %(x,y)) #将x上物体移到y上
    return



def Move_Tower(n, a, b, c):
    count = 0
    if (n == 1):
        print(a, "==>", c)                # 将最后一个盘子移动到 c 上
        return 1                          # 移動一次                 
    else:
        count += Move_Tower(n-1, a, c, b) # 将 n-1 个盘子移动到 b 上，b 相当于一个缓冲区
        count += Move_Tower(1, a, b, c)   # 将 n-1 移动到 b 后, 将最后一个盘子直接放在 c 上
        count += Move_Tower(n-1, b, a, c) # 将 n-1 从缓冲区 b 移动到 c 上, 完成
        return count                      # 移動 count 次, 三階段 Move_Tower 的移動次數總合

 x = Move_Tower(5,'A','B','C')
 print(x)
