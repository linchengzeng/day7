# -*- coding:utf-8 -*-
#  Author:aling
class Animal:
    def __init__(self,name):
        self.name = name

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")
        #只要调用它就报错,在这里的作用是子类必须重构它，否则就会报错
class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'Woof !Woof!'

d = Dog('d1')
c = Cat('c1')

def animal_talk(obj):
    print(obj.talk())  ###用于替代d.talk,c.talk\

animal_talk(d)
animal_talk(c)
##真正需要实现多态则应该是
## Animal.talk(c)
## Animal.talk(d)
