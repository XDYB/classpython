# -*- coding: utf-8 -*-
# @Time    : 2019/2/11 15:45
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : manage.py
# @Software: PyCharm

from Flask_study.app import app

print('* ━━━━━━神兽出没━━━━━━')
print('* 　　　┏┓　　　┏┓')
print('* 　　┏┛┻━━━┛┻┓')
print('* 　　┃　　　　　　　┃')
print('* 　　┃　　　━　　　┃')
print('* 　　┃　┳┛　┗┳　┃')
print('* 　　┃　　　　　　　┃')
print('* 　　┃　　　┻　　　┃')
print('* 　　┃　　　　　　　┃')
print('* 　　┗━┓　　　┏━┛Code is far away from bug with the animal protecting')
print('* 　　　　┃　　　┃    神兽保佑,代码无bug')
print('* 　　　　┃　　　┃')
print('* 　　　　┃　　　┗━━━┓')
print('* 　　　　┃　　　　　　　┣┓')
print('* 　　　　┃　　　　　　　┏┛')
print('* 　　　　┗┓┓┏━┳┓┏┛')
print('* 　　　　　┃┫┫　┃┫┫')
print('* 　　　　　┗┻┛　┗┻┛')
print('*')
print('* ━━━━━━感觉萌萌哒━━━━━━')




if __name__ == '__main__':
    print(app.url_map)  # 查看路由映射
    app.run(host='0.0.0.0', port=81)# 启动web服务器