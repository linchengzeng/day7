# -*- coding:utf-8 -*-
#  Author:aling
import pickle
# '''
# #写法1
# data0= {'defag':'123'}
# print('原始数据：%s'%data0)
# data1 = pickle.dumps(data0)
# print('序列化数据:',data1)
# with open('../db_files/users.txt','wb+') as fp:
#     fp.write(data1)
# with open('../db_files/users.txt','rb+') as fp:
#     print('返序列化数据:',pickle.loads(data1))
#
# '''

# #写法2
# data0= {'aling':'123'}
# print('原始数据：%s'%data0)
# with open('../db_files/users.txt','ab+') as fp:
#     pickle.dump(data0,fp)
#     fp.write(b'\n')
#
# with open('../db_files/users.txt','rb+') as fp:
#     for line in fp:
#         # data1 = pickle.load(fp.lin)
#         print('返序列化数据:',pickle.loads(line))


with open('../db_files/course_manage.db','rb') as fp:
    data = pickle.load(fp)
for line in data:
    print(line.ID)

