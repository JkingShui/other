在Python2版本中编写类时，默认不加载object。那加载object和不加载object的区别在哪里呢？

## 一是拥有的高级特性不同。
继承object可以拥有许多高级特性，这些高级特性是编写框架和大型项目时需要使用的，十分有用。

链接https://blog.csdn.net/DeepOscar/article/details/80947155中有继承object与不继承object两者特性的详细的表格

## 二是调用顺序不同。
继承了object的是新式类，不继承 object 的是经典类，在 Python 2 里面新式类和经典类在多继承调用顺序方面会有差异。具体而言就是经典类按照深度优先进行调用，而新式类遵循广度优先进行调用。

比如下面的代码，深度优先调用就是先从D->B->A->C，而广度优先则是D->B->C->A。

具体的调用顺序按照mro列表顺序，可以使用mro（）函数来查看mro列表。

```python
class A(object):
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

d=D()
print(D.mro())

>>>[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```



顺便一提，查找父类的函数super()实际上和父类并没有关系，它返回的是MRO列表中的下一个类。因此在单线程的类中返回的就是上一级的父类而已。

一般而言，使用新式类对多继承的处理更符合逻辑，所以基于这两点提倡大家在创建类时继承object。

在Python3的版本中，新建的类默认加载了object（即使你不写object），即拥有object的特性和广度优先的调用特点。但是基于书写规范，建议大家还是在类的后面添加上object。

