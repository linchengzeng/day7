# -*- coding:utf-8 -*-
#  Author:aling

from information_operator.edit_obj_infomation import Editor_info
from db_view.db_operator import Operator_db
class Update_teach_course_info(object):
    def update_t_c_info(self, user_data):
        '''
        :param: 更新老师授课信息
        :return:
        '''
        # print('update_teach_course.py in line 12')
        # search_old_info_all = Search_info()
        search_db = Operator_db()
        edit_classes = Editor_info()
        classes_obj_all = search_db.search_all_obj('classes_manage')
        if classes_obj_all:
            for classes_obj in classes_obj_all:
                if classes_obj.Class_Teacher.ID == user_data.ID:
                    print('\033[30;1m目前您所教的课程如下：\033[0m')
                    print('************************')
                    print('班级ID（唯一）：%s' % classes_obj.ID)
                    print('班级名称：%s' % classes_obj.Class_Name)
                    print('所教课程：%s' % classes_obj.Class_Course.Course_name)
            print('************************')
            # teach_edit_class = input('\033[30;1m请输入您需要更改的班级ID：\033[0m')
            # for classes_obj in classes_obj_all:
            #     if classes_obj.ID == teach_edit_class:
            #         edit_classes.editor_classes_info('classes_manage',classes_obj)
        else:
            print('\033[30;1m无法查到有效信息！请联系管理员再操作！\033[0m')