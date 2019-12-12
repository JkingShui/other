# coding: utf-8
from greenlet import greenlet
import greenlet as gt


def test1():
    print gt.getcurrent()   # 协程1
    print 1
    g2.switch()
    print 11


def test2():
    print 2
    g1.switch()
    print 22


print gt.getcurrent()       # 主协程
g1 = greenlet(test1)
g2 = greenlet(test2)
g1.switch()                 # 1 2 11
print gt.getcurrent()       # 主协程
print g1.dead               # True
print g2.dead               # False
g2.switch()                 # 22


u"""
    1.只有在test1函数是，是协程1
    2.22没有输出，原因是test2切换到test1后没有切换回来，等g2的引用计数清零是会
      抛出GreenletExit异常
    3.执行完对应的函数协程才会退出
    
    4.需要手动切换，不够智能
    
    5.GreenThread 作为greenlet的子类，添加了事件作为属性，官方建议使用spawn函数
      'get'一个greenthread，并将获得的greenthread交给hub来调度，等还有其他功能，
      实际是为greenlet添加了调度机制，极大地填补了greenlet协程的弊端
"""
