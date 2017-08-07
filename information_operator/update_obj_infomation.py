# -*- coding:utf-8 -*-
#  Author:aling


from db_view import db_operator,database_info
from information_operator import public_search

import setting,style,main_master


BASE_PATH = setting.BASE_PATH

class Editor_info():

    def update_obj_info(obj_table):
        if obj_table == 'school_manage':
            Editor_info.editor_school_obj(obj_table)
        elif obj_table == 'teacher_manage':
            print('update_obj_infomation.py  line 19')
        elif obj_table == 'course_manage':
            Editor_info.editor_course_obj((obj_table))
        elif obj_table == 'student_manage':
            print('update_obj_infomation.py line 23')


    # 更新前后的学校信息
    def editor_school_obj(obj_table):
        print('修改%s操作'% style.menu_dict[obj_table])
        edit_obj_id = input('\033[31;1m请输入您需要修改的%s的ID>>：\033[0m'%style.menu_dict[obj_table])
        obj_info = db_operator.operator_db.search_id_in_db(edit_obj_id, obj_table)
        if obj_info == 'Fail':
            print('无法找到此信息，请确认后重新修改！')
        else:
            print('学校ID（唯一）：%s'%obj_info.ID)
            print('学校名称：%s'%obj_info.School_Name)
            print('学校地址：%s'%obj_info.School_Addr)
            print('联系电话：%s'%obj_info.School_Tel)
            print('*******************')
            print(style.school_menu_arrt)
            update_attr = input('\033[31;1m请输入您需要修改的信息\033[0m')
            if update_attr in style.school_attr:
                new_val = input('\033[31;1m请输入新值>>：\033[0m')
                rank_val = style.school_attr[update_attr]
                try:
                    # 执行更新学校信息操作
                    new_obj_info = Editor_info.update_school_info(obj_info,obj_info.ID,rank_val,new_val,obj_table)
                    print('》》》》更新完成，更新后的信息为》》》》')
                    print('学校ID（唯一）：%s' % new_obj_info.ID)
                    print('学校名称：%s' % new_obj_info.School_Name)
                    print('学校地址：%s' % new_obj_info.School_Addr)
                    print('联系电话：%s' % new_obj_info.School_Tel)
                    print('*******************')
                except:
                    print('系统异常，更新信息失败，请联系管理员！')
        return main_master.manage_view

    # 更新前后的课程信息
    def editor_course_obj(obj_table):
        print('修改%s操作'% style.menu_dict[obj_table])
        edit_obj_id = input('\033[31;1m请输入您需要修改的%s的ID>>：\033[0m'%style.menu_dict[obj_table])
        obj_info = db_operator.operator_db.search_id_in_db(edit_obj_id, obj_table)
        if obj_info == 'Fail':
            print('无法找到此信息，请确认后重新修改！')
        else:
            print('课程ID（唯一）：%s'%obj_info.ID)
            print('课程名称：%s'%obj_info.Course_name)
            print('课程周期：%s'%obj_info.Course_period)
            print('课程费用：%s'%obj_info.Course_cost)
            print('********课程额外信息**********')
            print('开课地址：%s' % obj_info.Course_School.School_Addr)
            print('联系电话：%s' % obj_info.Course_School.School_Tel)
            print(style.course_menu_arrt)
            update_attr = input('\033[31;1m请输入您需要修改的信息\033[0m')
            if update_attr in style.school_attr:
                new_val = input('\033[31;1m请输入新值>>：\033[0m')
                rank_name = style.course_attr[update_attr]
                try:
                    new_obj_info = Editor_info.update_course_info(obj_info, obj_info.ID, rank_name, new_val, obj_table)
                    print('》》》》更新完成，更新后的信息为》》》》')
                    print('课程ID（唯一）：%s' % new_obj_info.ID)
                    print('课程名称：%s' % new_obj_info.Course_name)
                    print('课程周期：%s' % new_obj_info.Course_period)
                    print('课程费用：%s' % new_obj_info.Course_cost)
                    print('********课程额外信息**********')
                    print('开课地址：%s' % new_obj_info.Course_School.School_Addr)
                    print('联系电话：%s' % new_obj_info.Course_School.School_Tel)
                except:
                    print('系统异常，更新信息失败，请联系管理员！')
        return main_master.manage_view

    # 执行更新学校信息操作
    def update_school_info(obj, ID, obj_rank, new_val, obj_table):
        # 读取所有信息
        all_obj_info = public_search.Public_search_all.search_obj_all(obj_table)
        for line in all_obj_info:
            # 判断是本次需要修改的信息ID时进行删除
            if ID == line.ID:
                all_obj_info.remove(line)
        # 新建一个新的对象，并将新的值写入新对象
        if obj_rank == 'School_Name':
            #改名称
            new_obj = database_info.School(obj.ID, new_val, obj.School_Addr, obj.School_Tel)
        elif obj_rank =='School_Addr':
            #改地址
            new_obj = database_info.School(obj.ID, obj.School_Name, new_val,  obj.School_Tel)
        elif obj_rank == 'School_Tel':
            #改电话
            new_obj = database_info.School(obj.ID, obj.School_Name, obj.School_Addr, new_val)
        #将更新后的对象添加到原来的数据库表中
        all_obj_info.append(new_obj)
        #数据持久化到文件中
        db_operator.operator_db.fulsh_db(all_obj_info,obj_table)
        return new_obj

    # 更新课程信息
    def update_course_info(obj_info, ID, rank_name, new_val, obj_table):
        # 读取所有信息
        all_obj_info = public_search.Public_search_all.search_obj_all(obj_table)
        for line in all_obj_info:
            # 判断是本次需要修改的信息ID时进行删除
            if ID == line.ID:
                all_obj_info.remove(line)
        # 新建一个新的对象，并将新的值写入新对象
        if rank_name == 'Course_Name':
            # 改课程名称
            new_obj = database_info.Course(obj_info.ID, new_val, obj_info.Course_Period, obj_info.Course_Cost, obj_info.Course_School)
        elif rank_name == 'Course_Period':
            # 改地址
            new_obj = database_info.Course(obj_info.ID, obj_info.Course_Name, new_val, obj_info.Course_Cost, obj_info.Course_School)
        elif rank_name == 'Course_Cost':
            # 改电话
            new_obj = database_info.Course(obj_info.ID, obj_info.Course_Name, obj_info.Course_Period, new_val, obj_info.Course_School)
        # 将更新后的对象添加到原来的数据库表中
        all_obj_info.append(new_obj)
        # 数据持久化到文件中
        db_operator.operator_db.fulsh_db(all_obj_info, obj_table)
        return new_obj