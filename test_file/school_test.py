# -*- coding:utf-8 -*-
#  Author:aling
class SchoolMember(object):
    ''' 学校成员基类'''
    member = 0  #计数器，每增加一个学员加1

    def __init__(self,name,age,sex):
        '''
        :param name: 姓名
        :param age: 年龄
        :param sex: 性别
        '''
        self.NAME = name
        self.AGE = age
        self.SEX = sex
        self.enroll()###一实例化就自动注册
    def enroll(self):
        '''注册'''
        print('just enrolled a new school member [%s]'%self.NAME)
        SchoolMember.member +=1    #被实例化时加1

    def tell(self):
        print('打印%s的个人信息'%self.NAME)
        print('------my self info --------')
        for k,v in self.__dict__.items():
            print(k,":",v)

    def __del__(self):#当学生毕业时，从成员中删除
        print('%s 学员毕业'%self.NAME)
        SchoolMember.member -=1

class Teacher(SchoolMember): #继承SchoolMember类
    '''讲师类'''
    def __init__(self,name,age,sex,salary,course):
        '''
        :param name: 名称
        :param age: 年龄
        :param sex: 性别
        :param salary: 工资
        :param course: 所教课程
        '''
        SchoolMember.__init__(self,name,age,sex)
        self.SALARY = salary
        self.COURSE = course

    def teaching(self):
        print('Teacher %s is teaching [%s]'%(self.NAME,self.COURSE))

class Student(SchoolMember):  # 继承SchoolMember类
    def __init__(self,name,age,sex,course,tuition):
        '''
        :param name: 姓名
        :param age: 年龄
        :param sex: 性别
        :param course: 所学课程
        :param tuition: 学费
        '''
        SchoolMember.__init__(self,name,age,sex)
        self.COURSE=course
        self.TUITION = tuition
        self.amount = 0

    def pay_tutition(self,amount):
        print("student %s has just paied %s"%(self.NAME,amount))
        self.amount += amount  #有可能报很多课程

zs= Teacher("张三",28,"F*M",3000,"Python")
lis = Student("李四",18,"N/A","PYS15",30000)
ww= Student("王五",19,"M","PYS15",11000)

print(SchoolMember.member)
del ww  ##测试析构函数的作用
print(SchoolMember.member)

####打印成员的所有信息
print(zs.__dict__)
print('-------或以下这种方式-----')
zs.tell()