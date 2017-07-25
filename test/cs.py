# -*- coding:utf-8 -*-
#  Author:aling
class Role(object):
    def __init__(self,name,role,tool,wages=1000):
        self.NAME = name,
        self.ROLE = role,
        self.TOOL = tool,
        self.WAGES = wages

    def teach(self):
        print("%s 在上课"%self.NAME)

    def texercises(self):
        print("%s在改作业"%self.NAME)

    def payoff(self,wage):
        print("%s调工资%s"%(self.NAME,wage))
        self.WAGES = wage
r1=Role('张三','police','cat')#生成一个对象
r2=Role('赵四','teacher','book')#生成一个对象

r1.payoff(2000)

print(r1.WAGES)