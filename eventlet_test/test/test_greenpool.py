# coding:utf-8

from eventlet import greenpool


gp = greenpool.GreenPool(size=1000)


def fun(a,  b):
    return a + b


gt = gp.spawn(fun, 1, 2)
print gt.wait()
