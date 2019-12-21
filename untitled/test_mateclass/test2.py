# -*- coding:utf-8 -*-


class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)  # eg: <IntegerField:id>


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'int')


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(50)')


# attrs 是 类的属性集合
# __mappings__  __table__是自己添加的两个属性,他两在使用该元类创建的父类 Model中也能获取到
class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":  # 不是实际使用的类,跳过
            return type.__new__(cls, name, bases, attrs)
        mapping = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                mapping[k] = v
        for k in mapping.keys():
            attrs.pop(k)  # 从类属性中删除该Field属性 否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）
            # 实例 User(id=1234,..) 但是User类中也有id等属性
        attrs['__mappings__'] = mapping  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 添加属性__table__存放准备创建的类的名字, 也就是表的名字
        # 这样一来,父类Model才能获取它未出生的儿子的类名

        return type.__new__(cls, name, bases, attrs)


class Model(dict):

    # 指示使用ListMetaclass来定制类，传入关键字参数metaclass
    __metaclass__ = ModelMetaClass

    def __init__(self, **kw):
        return super(Model, self).__init__(**kw)

    def __getattr__(self, key): #m.key==>m[key]
        try:
            return self[key]
        except KeyError as e:
            raise AttributeError(r"'Model' object has no attribute %s" % key)

    def __setattr__(self, name, value):# m.key=value ==> m[key]=value
        self[name] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name) # v是一个Field对象
            params.append('?') # sql的占位符 ?
            args.append(getattr(self, k, None))

        # 模拟一下数据库操作
        sql = 'insert into %s (%s) values (%s)' % (self.__table__,
                                                   ','.join(fields),
                                                   ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


# 到使用部分就简单了
class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


# 下面实例化时的 id name等会和 上面的类的成员变量同名冲突, 幸好在元类里面attrs.pop()掉了
u = User(id=1234, name='xcl', email='chunlaixiao@163.com', password='123456')
u2 = User(id=788, name='wang', email='wang@163.com', password='123456')

u.save()
u2.save()
# 这是调用__getattr__()方法 返回u[name]
print(u.name)
