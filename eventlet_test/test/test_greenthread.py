# -*- coding:utf-8 -*-

u"""
greenlet 怎么上升到 greenthread？
Hub构成了 Eventlet 的事件循环，它分发 I/O 事件、调度 greenthread。
Hub的存在使得协程被提升为 greenthreads


hub = hubs.get_hub()
hub.switch()
切换到主协程


· greenthread中_exit_event这个事件对象的作用
    1.将greenthread要执行函数的执行结果直接_exit_event.send，这样最大的好处
      就是，即把结果可以保存，又可以执行之后的操作，提供了协程退出后，
      可以执行‘退出函数’的能力，比直接return更好
    2.提供了wait机制，在协程wait时，调度器可以将协程切出去，执行其他协程的任务
"""

from eventlet import greenthread
import greenlet


def add(a, b, **kwargs):
    return a + b


def _exit_funcs(*args, **kwargs):
    print '========='


gt = greenthread.GreenThread(greenlet.getcurrent())

# link 用来绑定协程退出函数
gt.link(_exit_funcs)

# main 函数执行用户的函数，执行完成之后将结果通过事件send出去
# 然后 如果有link的函数就会执行，且将_resolving_links = False，
# 表示没有需要执行的退出函数（没有 link）
gt.main(add, [1, 2], {})

# 通过wait的到add执行结果
print gt.wait()

u"""假想的greenthread 调度机制（待验证）

    1、创建好协程
    2、link 设置退出函数（如果有必要）
    3、通过main函数执行user_func
    4、通过wait等待执行结果
    5、切换到其他协程
"""
