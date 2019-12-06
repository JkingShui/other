# coding=utf-8
u"""
    Pool class implements resource limitation and construction.

    There are two ways of using Pool: passing a `create` argument or
    subclassing. In either case you must provide a way to create
    the resource.

    第一种： 使用子类的方式
        class Test(object):
            pass

        class TestPool(pools.Pool):
            def create(self):
                return Test()

        p = TestPool(min_size=5, max_size=10)

    第二种：使用参数的方式
        class Test(object):
            pass

        p = pools.Pool(min_size=5, max_size=10, create=lambda:Test())

"""
from eventlet import pools


class Test(object):
    pass


class TestPools(pools.Pool):
    def create(self):
        return Test()


pool = TestPools(min_size=5, max_size=10)

# print type(pool.get())
# print type(pool.get())
# print type(pool.get())
# print type(pool.get())
# print type(pool.get())
# print type(pool.get())
# print type(pool.get())
# print type(pool.get())
# print type(pool.get())
# print type(pool.get())
# print type(pool.get())
#
# print pool.current_size
# print pool.free()
print pool.current_size
print pool.free()

with pool.item() as tp:
    print type(tp)

print pool.current_size
print pool.free()

test_pool = pool.get()
print pool.current_size
print pool.free()

pool.put(test_pool)
print pool.current_size
print pool.free()


u"""
总结：
    1. pool 可设置min_size和max_size， 当我们创建一个pool对象是，会创建min_size
       个对象，放在free_items这个deque中，当get时，会先从free_items中获取，如果
       free_items中没有就会创建资源，创建的资源超过最大值会放入等待队列等待
    2. put 是将get到的资源放回池中，先判断等待队列有没有等待，有的话优先处理等待
       的，没有的话，将资源放入空闲队列
    
    3. 有两种用法：
        ·前置：
            class Test(object):
                pass

            class TestPools(pools.Pool):
                def create(self):
                    return Test()
                    
            pool = TestPools(min_size=5, max_size=10)
        a) 手动申请，手动释放
            要使用资源时 p = pool.get()
            使用完之后 pool.put(p)
        
        b) 使用with达到自动申请/释放的目的
            with pool.item() as tp:
                print type(tp)
            
"""

