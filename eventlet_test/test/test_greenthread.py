# -*- coding:utf-8 -*-

u"""
greenlet 怎么上升到 greenthread？
Hub构成了 Eventlet 的事件循环，它分发 I/O 事件、调度 greenthread。
Hub的存在使得协程被提升为 greenthreads


hub = hubs.get_hub()
hub.switch()
切换到主协程

"""
