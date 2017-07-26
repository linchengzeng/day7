# -*- coding:utf-8 -*-
#  Author:aling
import sys,os
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.dirname(FILE_PATH)
sys.path.append(BASE_PATH)
print(BASE_PATH)