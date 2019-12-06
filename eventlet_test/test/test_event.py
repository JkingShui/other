# coding=utf-8
u"""
1.一个事件只能send一次，想要再次send，需要重新创建一个Event对象
2.wait 等待直到另一个协程调用 send() 。返回其他协程传递给 send() 方法的值
3.ready判断一个事件是否已经send， 已经send返回True， 否则返回False
4.send_exception(*args) 发送一个异常，  例如：evt.send_exception(RuntimeError())
5.reset：一个事件send之后，不能再次send，但是reset之后可以发送

TODO :
1. 生产者消费者模型   socket
"""
from eventlet import event
import eventlet


evt = event.Event()


def baz(b):
    evt.send(b + 1)


_ = eventlet.spawn_n(baz, 3)


print evt.ready()
print evt.wait()
print evt.ready()

evt.reset()
evt.send(2)
print evt.wait()
