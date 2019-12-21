# coding: utf-8


def upper_attr(class_name, class_parents, class_attr):

    # class_name 会保存类的名字 Foo
    # class_parents 会保存类的父类 object
    # class_attr 会以字典的方式保存所有的类属性

    # 遍历属性字典，把不是__开头的属性名字变为大写
    new_attr = {}
    print("="*30)
    for name, value in class_attr.items():
        print("name=%s and value=%s" % (name, value))  # 打印所有类属性出来
        if not name.startswith("__"):
            new_attr[name.upper()] = value
            print("name.upper()=", name.upper())
            print("value=", value)

    # 调用type来创建一个类
    return type(class_name, class_parents, new_attr)


class Foo(object):
    # 设置Foo类的元类为upper_attr
    __metaclass__ = upper_attr

    bar = 'bip'

    # def __init__(self):
    #     pass
    #
    # def fun(self):
    #     print '= fun ='


print("="*30)
print("check Foo exist bar attr=",hasattr(Foo, 'bar'))
print("check Foo exist BAR attr=",hasattr(Foo, 'BAR'))

f = Foo()
print("print f.BAR=", f.BAR)


u"""output
==============================
name=bar and value=bip
('name.upper()=', 'BAR')
('value=', 'bip')
name=__module__ and value=__main__
name=__metaclass__ and value=<function upper_attr at 0x0000000001E0B5F8>

==============================
('check Foo exist bar attr=', False)
('check Foo exist BAR attr=', True)
('print f.BAR=', 'bip')

    由输出结果可以看出：
        __metaclass__ 指向的可调用对象会在类创建时调用，但是就是类名、基类、类成员
        最终返回的使用type创建的类
        
"""