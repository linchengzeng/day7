# -*- coding:utf-8 -*-
#  Author:aling

import sys, time, os, main_master


if __name__ == '__main__':

    #将项目目录加入系统环境变量
    BASE_PATH = os.path.dirname(__file__)
    SUPER_PATH = os.path.dirname(BASE_PATH)
    sys.path.append(os.path.dirname(SUPER_PATH))


    print('系统正在加载中，请稍候！')

    for i in range(30):
        sys.stdout.write('#')
        sys.stdout.flush()
        time.sleep(0.1)
        if i == 15:
            sys.stdout.write('欢迎使用简易校园管理系统')
    print('\n\033[30;1m本系统暂不提供用户自行注册，若需使用本系统，请联系管理员添加用户！\033[0m')
    main_master.main_page()
    # logging.info(main_master)