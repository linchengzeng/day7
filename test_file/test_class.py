# -*- coding:utf-8 -*-
#  Author:aling
class Person(object):
    def __init__(self,name,age):   #self = b,   self.name = b.name
        self.name = name
        self.age = age
    def talk(self):
        print('person is talking.....')

class BlackPerson(Person):
    def __init__(self,name,age,power):#先继承，再重构
        Person.__init__(self,name,age)
        self.power = power
        # print(self.name)   #继承后就可以直接使用了
        # print(self.age)    #继承后就可以直接使用了
    def talk(self):
        print("I'm %s ,my age %s,my power is %s"%(self.name,self.age,self.power))
    def walk(self):
        print("is walking .....")

class WritePerson(Person):
    pass

b = BlackPerson('aling',22,'Noraml')
b.talk()
b.walk()

