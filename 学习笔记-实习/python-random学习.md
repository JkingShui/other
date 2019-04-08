## Python random()函数

**random()方法五参数，返回一个随机数，它在[0,1)范围内**

```python
import random
print(random.random())
#结果为：0.033666764911409186（每次执行结果不同）
```



**random中的常见函数**

```python
import random

print(random.randint(1, 100))      #产生1到100的随机数
print(random.random())             #产生0到1之间的随机浮点数
print(random.uniform(1.1, 5.4))    #产生一个1.1到5.4的随机浮点数
print(random.choice('tomorrow'))   #从序列中随机选取一个元素

print(random.randrange(1, 100, 2)) #生成从1到100随机整数x，下一个随机数不在[x-2, x+2]范围内

a = [1, 3, 4, 5, 8]
random.shuffle(a)                  #将序列a中的元素顺序打乱
print(a)

print(random.sample('zyxwvutsrqponmlkjihgfedcba',5))# 多个字符中生成指定数量的随机字符：

print random.choice(['剪刀', '石头', '布']) # 随机选取字符串
```





