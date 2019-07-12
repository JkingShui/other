## JSON模块

JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式。它基于ECMAScript的一个子集。 JSON采用完全独立于语言的文本格式，但是也使用了类似于C语言家族的习惯(包括C、C++、Java、JavaScript、Perl、Python等)。这些特性使JSON成为理想的数据交换语言。易于人阅读和编写，同时也易于机器解析和生成(一般用于提升网络传输速率)。

JSON在python中分别由list和dict组成。

Json模块提供了四个功能：dumps、dump、loads、load

### dumps 将python中的 字典 转换为 字符串

```python
import json

test_dirc = {"begberg": [7600, {"1": [["iphone", 6300], ["bike", 800], ["shirt", 300]]}]}
print(test_dirc)
print(type(test_dirc))
#dumps将数据转换成字符砖
json_str = json.dumps(test_dirc)
print(json_str)
print(type(json_str))
```

结果：

```json
{'begberg': [7600, {'1': [['iphone', 6300], ['bike', 800], ['shirt', 300]]}]}
<class 'dict'>
{"begberg": [7600, {"1": [["iphone", 6300], ["bike", 800], ["shirt", 300]]}]}
<class 'str'>
```

### loads: 将 字符串 转换为 字典

```python
new_dirc = json.loads(json_str)
print(new_dirc)
print(type(new_dirc))
```

结果：

```json
{'begberg': [7600, {'1': [['iphone', 6300], ['bike', 800], ['shirt', 300]]}]}
<class 'dict'>
```

### dump: 将数据写入json文件中

```python
with open("test.json", "w") as f:
    json.dump(new_dirc, f)
    print("写入成功！")
```

结果：

```json
#test.json中的数据，原来的数据会被覆盖，这与打开方式有关系，与dump无关
{"begberg": [7600, {"1": [["iphone", 6300], ["bike", 800], ["shirt", 300]]}]}
```

### load:把文件打开，并把字符串变换为数据类型

```python
with open('test.json', 'r') as load_f:
    load_dirc = json.load(load_f)
    print(load_f)
    print(type(load_f))

load_dirc['smallberg'] = [8200,{1:[['Python',81],['shirt',300]]}]
print(load_dirc)
print(type(load_f))

with open('test.json', 'w') as dump_f:
    json.dump(load_dirc, dump_f)
```

结果：

```json
#控制台打印出
<_io.TextIOWrapper name='test.json' mode='r' encoding='cp936'>
<class '_io.TextIOWrapper'>
{'begberg': [7600, {'1': [['iphone', 6300], ['bike', 800], ['shirt', 300]]}], 'smallberg': [8200, {1: [['Python', 81], ['shirt', 300]]}]}
<class 'dict'>

#test.json中的内容
{"begberg": [7600, {"1": [["iphone", 6300], ["bike", 800], ["shirt", 300]]}], "smallberg": [8200, {"1": [["Python", 81], ["shirt", 300]]}]}
```

