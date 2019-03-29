##isinstance

-------------------
[TOC]

###描述
Python中的 isinstance() 函数，是Python中的一个内置函数，用来判断一个函数是否是一个已知的类型，类似 type()。

###语法
```python
def	isinstance(object,classinfo)
```

###参数
+ object : 实例对象。
+ classinfo : 可以是直接或者间接类名、基本类型或者由它们组成的元组。

###实例
```python
a = 2
isinstance(a, int) #返回True
isinstance(a, str) #返回False
isinstance(a, (str, int, list)) #是元组中的一个，结果返回True
```

###isinstance()与type()的区别
在继承上的区别：
+ isinstance() 会认为子类是一种父类类型，考虑继承关系。
+ type() 不会认为子类是一种父类类型，不考虑继承关系。

```python
class A:
    pass

class B(A):
    pass

isinstance(A(), A)    # returns True
type(A()) == A        # returns True
isinstance(B(), A)    # returns True
type(B()) == A        # returns False
```