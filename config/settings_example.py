# Author: dz2h1
# inspection's settings
import pymongo


ver = 'V0.2.0'  # 网页右上角的版本显示
mongodb_add = '192.168.1.1'  # mongodb数据库地址
mongodb_port = 27017  # 数据库端口，默认27017
logs_find_limit = 30  # log页面最大展示条目数量
charts_dis_num_limit = 12  # chart页面每个图表数据历史数量
pageSizeChangeUpper = 105  # size页面变化正常上限，单位（%）
pageSizeChangelower = 95  # size页面变化正常下线，单位（%），超过上下限将触发报警
reportSetTime = '0830'  # 巡检邮件报告时间
python_path = '/usr/bin/python3'  # python命令的地址，用于报警脚本执行
sendMail_fileName = '/check_send_mail.py'  # 报警脚本名称，win环境下为'/check_send_mail_win.py'
'''
v0.1.2版本中支持企业微信消息报警
在check_base中选择注释from crontab_mail.XXX_settings启用功能
'''


def mongo_clinet():
    ''' inspection数据库接口函数'''
    return pymongo.MongoClient(host=mongodb_add,
                               port=mongodb_port,
                               connect=False)


def mongo_name():
    ''' inspection数据库用户名'''
    return 'admin'


def mongo_password():
    ''' inspection数据库密码，可修改为从环境变量读取用户名密码'''
    return '123456'
