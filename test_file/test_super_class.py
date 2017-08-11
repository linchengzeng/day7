# -*- coding:utf-8 -*-
#  Author:aling

class School():
    def __init__(self, ID, school_name, school_addr, school_tel):
        self.ID = ID
        self.School_Name = school_name
        self.School_Addr = school_addr
        self.School_Tel = school_tel

class Course():
    def __init__(self, ID, course_name, course_period, course_cost, School):
        self.ID = ID
        self.Course_name = course_name
        self.Course_period = course_period
        self.Course_cost = course_cost
        self.Course_School = School

# **********************************

class School():
    def __init__(self, ID, school_name):
        self.ID = ID
        self.School_Name = school_name

    def add_course(self,course_id,course_name, course_period, course_cost, School):
        result = Course(course_id,course_name, course_period, course_cost, School)

class Course():
    def __init__(self, ID, course_name, course_period, course_cost, School):
        self.ID = ID
        self.Course_name = course_name
        self.Course_period = course_period
        self.Course_cost = course_cost
        self.Course_School = School