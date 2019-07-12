## 多线程

> Python3 通过两个标准库 _thread 和 threading 提供对线程的支持。_
>
> thread 提供了低级别的、原始的线程以及一个简单的锁，它相比于 threading 模块的功能还是比较有限的。
>
> + threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法：
> + **threading.currentThread()**: 返回当前的线程变量。
> + **threading.enumerate()**: 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。



**threading.activeCount()**: 返回正在运行的线程数量，与**len(threading.enumerate())**有相同的结果。

除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:

​	**a.** **run():** 用以表示线程活动的方法。

​	**b.** **start():**启动线程活动。

​	**c.** **join([time]):** 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。

​	**d.** **isAlive():** 返回线程是否活动的。

​	**e.** **getName():** 返回线程名。

​	**f.** **setName():** 设置线程名。

```python
import threading
import time

exitFlag = 0

class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def print_time(threadName, delay, counter):
        while counter:
            if exitFlag:
                threadName.exit()
            time.sleep(delay)
            print("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1

    def run(self):
        print('开始线程：' + self.name)
        MyThread.print_time(self.name, self.counter, 5)
        print('结束线程：' + self.name)

#创建线程
thread1 = MyThread(1, 'Thread-1', 1)
thread2 = MyThread(2, 'Thread-2', 2)

#启动线程
thread1.start() #启动线程，即调用了run方法
thread2.start()

#等待线程
thread1.join()
thread2.join()

print('退出主线程')
```

运行结果：

```
开始线程：Thread-1
开始线程：Thread-2
Thread-1: Wed Apr 10 15:40:02 2019
Thread-2: Wed Apr 10 15:40:03 2019
Thread-1: Wed Apr 10 15:40:03 2019
Thread-1: Wed Apr 10 15:40:04 2019
Thread-2: Wed Apr 10 15:40:05 2019
Thread-1: Wed Apr 10 15:40:05 2019
Thread-1: Wed Apr 10 15:40:06 2019
结束线程：Thread-1
Thread-2: Wed Apr 10 15:40:07 2019
Thread-2: Wed Apr 10 15:40:09 2019
Thread-2: Wed Apr 10 15:40:11 2019
结束线程：Thread-2
退出主线程
```

## 线程锁

> 如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步。
>
> 使用 Thread 对象的 Lock 和 Rlock 可以实现简单的线程同步，这两个对象都有 acquire 方法和 release 方法，对于那些需要每次只允许一个线程操作的数据，可以将其操作放到 acquire 和 release 方法之间。如下：

```python

```

