# -*- coding:utf-8 -*-
#  Author:aling
import pickle,hmac
data = {'aling':'123'}
hash = hmac.new(b'aling',b'123')
print(hash.hexdigest())
# with open('../db_files/users.db','wb+') as fp:
# data1 = pickle.dumps(hash.digest())
# data = ['abc','defg','hijklm']

data1= {'aling':'123'}
#
# print('加密前数据:aling')
# hash1 = hmac.new(bytearray(data0))
# hash1.update(b'123')
# data0_hash = hash1.hexdigest()
# print('加密后算法%s'%data0_hash)
# data1 = pickle.dumps(hash1)
#
# # with open('../db_files/users.db','rb') as fp:
data2 = pickle.loads(data1)
print('原始数据：%s'%data1)
print('序列化后数据：%s'%data1)
print('反序列化后数据：%s'%data2)


print('########################')
