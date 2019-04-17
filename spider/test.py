# -*- coding:UTF-8 -*-
'''
    requests.request()      构造一个请求，支撑一下更方法
    requests.get()          获取HTML页面的主要方法，对应去HTTP的GET
    requests.head()         获取HTML页面的主要方法，对应去HTTP的HEAD
    requests.post()         向HTML页面提交POST请求的方法，对应去HTTP的POST
    requests.put()          向HTML页面提交PUT请求的方法，对应去HTTP的PUT
    requests.patch()        向HTML页面提交局部修改请求，对应去HTTP的PATCH
    requests.delete()       获取HTML页面提交删除请求，对应去HTTP的DELETE
'''
import requests

if __name__ == '__main__':
    target = 'http://gitbook.cn/'
    req = requests.get(url=target)
    print(req.text)
