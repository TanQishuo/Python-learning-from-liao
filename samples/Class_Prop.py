# -*- coding: utf-8 -*-
"""
Created on Tue May 15 14:37:19 2018

@author: 123456
"""

#为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1
# 测试:
if Student.count != 0:
    print('测试失败1!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败2!')
    else:
        lisa = Student('lisa')
        if Student.count != 2:
            print('测试失败3!')
        else:
            print('Students:', Student.count)
            print('测试通过!')