# -*- coding:utf-8 -*-
#  Author:aling
class SchoolMember(object):
    ''' 学校成员基类'''
    def __init__(self,name,age,sex):
        self.NAME = name
        self.AGE = age
        self.SEX = sex

class Person(object):
    def open_branch(self,addr):
        print('openning a new branch in ',addr)

class Teacher(SchoolMember,Person): #继承SchoolMember类，又继承Person类
    '''讲师类'''
    def __init__(self,name,age,sex,salary,course):
        SchoolMember.__init__(self,name,age,sex)
        self.SALARY = salary
        self.COURSE = course

    def teaching(self):
        print('Teacher %s is teaching [%s]'%(self.NAME,self.COURSE))


zs= Teacher("张三",28,"F*M",3000,"Python")
zs.teaching()
zs.open_branch('SH')
