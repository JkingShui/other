[TOC]



# 装饰器

- 带固定参数的装饰器

```python
import time

def deco(f):
    def wrapper(a,b):
        start_time = time.time()
        f(a,b)
        end_time = time.time()
        execution_time = (end_time - start_time)*1000
        print("time is %d ms" % execution_time)
    return wrapper

@deco
def f(a,b):
    print("be on")
    time.sleep(1)
    print("result is %d" %(a+b))

if __name__ == '__main__':
    f(3,4)
```

- 无固定参数的装饰器

```python
import time

def deco(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        f(*args, **kwargs)
        end_time = time.time()
        execution_time_ = (end_time - start_time)*1000
        print("time is %d ms" %execution_time)
    return wrapper


@deco
def f(a,b):
    print("be on")
    time.sleep(1)
    print("result is %d" %(a+b))

@deco
def f2(a,b,c):
    print("be on")
    time.sleep(1)
    print("result is %d" %(a+b+c))


if __name__ == '__main__':
    f2(3,4,5)
    f(3,4)
```

## 随便写写

```python
class _test(object):
    def __init__(self):
        print '__init__'

    def __call__(self, *args, **kwargs):
        print '__call__'

    def __getattr__(self, item):
        print item


def test(*args, **kwargs):
    return _test()


@test(a='aa', b='cc')
def fun():
    print '__fun__'
    
结果：
__init__
__call__
可以看出 __fun__ 没被打印
```



## 自己的理解

1. 装饰器就是在函数前后添加一些操作，也有能力不让函数执行，这个看具体代码
2. 在执行时，