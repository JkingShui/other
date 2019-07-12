**Python中的魔术方法详解**

```在Python中，所有以“__”双下划线包起来的方法，都统称为“Magic Method”，中文称『魔术方法』,例如类的初始化方法 __init__,Python中所有的魔术方法均在官方文档中有相应描述，但是对于官方的描述比较混乱而且组织比较松散。很难找到有一个例子。```

+++



[TOC]

##  构造和初始化

> `__init__ `：通过此方法我们可以定义一个对象的初始操作，<u>用来初始化对象</u>
>
> `__new__`：`__init__` 并不是第一个被调用的方法。实际上，还有一个叫做`__new__ `的方法，两个共同构成了“构造函数”，<u>返回一个实例对象，可以理解为申请了一块空间，用来保存实例对象</u>
>
> `__del__`：可以将`__del__`理解为“构析函数”，<u>对象销毁时，调用的最后一个函数</u>

```python
from os.path import join 
class FileObject: 
    '''给文件对象进行包装从而确认在删除时文件流关闭'''
    
    def __init__(self, filepath='~', filename='sample.txt'): 
        #读写模式打开一个文件 
        self.file = open(join(filepath, filename), 'r+') 
        
    def __del__(self): 
        self.file.close() 
        del self.file
```

## 控制属性访问

>`__getattr__(self, name)`：当一个类对象访问一个类内没有的属性时(注意不是函数)，会调用这个方法，name保存的是调用的属性名
>
>`__setattr__(self, name, value)`：对一个类内没有的属性赋值时（注意不是函数），会调用这个方法，name保存的是属性名，value保存的是等号右边的值，实现`__setattr__`时要避免"无限递归"的错误。
>
>`__delattr__(slef):`：与 `__setattr__ `相同，但是功能是删除一个属性而不是设置他们。实现时也要防止无限递归现象发生。
>
>`__getattribute__(self, name)`:`__getattribute__`定义了你的属性被访问时的行为，相比较，`__getattr__`只有该属性不存在时才会起作用。因此，在支持`__getattribute__`的Python版本,调用`__getattr__`前必定会调用 `__getattribute__`。`__getattribute__`同样要避免"无限递归"的错误。需要提醒的是，最好不要尝试去实现`__getattribute__`,因为很少见到这种做法，而且很容易出bug。

```python
class A(object):
    def __getattr__(self, name):
        print('call __getattr__')
        print(name)

    def __setattr__(self, name, value):
        print('call __setattr__')
        print(name)
        print(value)

obj.c = 100    #调用__setattr__
print(obj.c)   #调用__getattr__
```



## 自定义容器的magic method

返回容器的长度。对于可变和不可变容器的协议，这都是其中的一部分。

```python
`__len__(``self``):`
```

定义当某一项被访问时，使用self[key]所产生的行为。这也是不可变容器和可变容器协议的一部分。如果键的类型错误将产生TypeError；如果key没有合适的值则产生KeyError。

```python
`__getitem__(``self``, key):`
```

当你执行self[key] = value时，调用的是该方法。

```python
`__setitem__(``self``, key, value):`
```

定义当一个项目被删除时的行为(比如 del self[key])。这只是可变容器协议中的一部分。当使用一个无效的键时应该抛出适当的异常。

```python
`__delitem__(``self``, key):`
```

返回一个容器迭代器，很多情况下会返回迭代器，尤其是当内置的iter()方法被调用的时候，以及当使用for x in container:方式循环的时候。迭代器是它们本身的对象，它们必须定义返回self的`__iter__`方法。　　

```python
`__iter__(``self``):`
```

实现当reversed()被调用时的行为。应该返回序列反转后的版本。仅当序列可以是有序的时候实现它，例如对于列表或者元组。

```python
`__reversed__(``self``):`
```

定义了调用in和not in来测试成员是否存在的时候所产生的行为。你可能会问为什么这个不是序列协议的一部分？因为当`__contains__`没有被定义的时候，如果没有定义，那么Python会迭代容器中的元素来一个一个比较，从而决定返回True或者False。

```python
`__contains__(``self``, item):`
```

dict字典类型会有该方法，它定义了key如果在容器中找不到时触发的行为。比如d = {'a': 1}, 当你执行d[notexist]时，d.`__missing__`['notexist']就会被调用。

```python
`__missing__(``self``, key):`
```



```__call__(``self``, [args...]):```

允许一个类的实例像函数一样被调用。实质上说，这意味着 x() 与 x.__call__() 是相同的。注意 __call__ 的参数可变。这意味着你可以定义 __call__ 为其他你想要的函数，无论有多少个参数。