# coding=utf-8
u"""
    Pool class implements resource limitation and construction.

    There are two ways of using Pool: passing a `create` argument or
    subclassing. In either case you must provide a way to create
    the resource.
"""
from eventlet import pools


class Test(object):
    pass


class TestPools(pools.Pool):
    def create(self):
        return Test()


pool = TestPools(min_size=5, max_size=10)

print type(pool.get())
print type(pool.get())
print type(pool.get())
print type(pool.get())
print type(pool.get())
print type(pool.get())
print type(pool.get())
print type(pool.get())
print type(pool.get())
print type(pool.get())
print pool.current_size

print type(pool.get())


print pool.current_size
print pool.free()

