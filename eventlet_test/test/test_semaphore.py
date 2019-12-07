# coding=utf-8


u""" eventlet.semaphore.Semaphore 信号量

    Semaphore 维护两个成员变量 :
        1) self.counter 信号量的剩余
        2) self._waiters 等待队列

    主要方法：
        1）acquire 获取信号量
            参数：blocking：是否是阻塞式获取    timeoute：超时时间
            a) if self.counter > 0
                计数减一， return True
            b) 计数为0， 等待队列有等待的协程
                在超时时间内尝试调度当前协程，成功True 超时False
            思想：  1.当信号量的计数器>0时，协程申请信号量只会将计数器-1
                      return True，来表示信号量申请成功
                    2.当信号量计数为0时，或者等待队列有协程时，表示当前不可申请信号量
                        1）当 设置为非阻塞式，且目前信号量计数为0时， 直接返回False
                        2）当信号量计数为0时，阻塞式获取信号量时，在超时时间内尝试被调度器调度
                            调度成功 return True   调度失败 return False
                            未设置超时时间则一直阻塞式获取

        2) release 释放信号量
            ·信号量的计数会+1
            ·如果等待队列有协程，就设置一个固定时间执行def _do_acquire(self)
              def _do_acquire(self)这个函数会将等待的协程拿出等待队列，然后尝试被调度


    如何使用可以看看greenpool

"""

