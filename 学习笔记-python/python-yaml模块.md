

## YAML格式

[相关播客](https://blog.csdn.net/liukuan73/article/details/78031693)



## Python中的YAML模块(yaml)

### 安装

```shell
pip insatll pyyaml
```

### 使用

```python
import yaml
with open('test.yaml', 'r') as test_yaml:
    #将yaml文件的内容加载到python作为一个python对象
	yaml_dict = load(test_yaml, Loader=yaml.SafeLoader)

# yaml.dump() 将从yaml文件加载来的字典转换成字符串，打印出来跟yaml的格式一样
yaml_str = yaml.dump()

# safe_load  安全的加载方式
with open('test.yaml', 'r') as test_yaml:
    yaml_dict = yaml.safe_load(test_yaml)

# safe_dump  安全的写入方式
with open('./xx.yaml', 'w+') as f:
    yaml.safe_dump(yaml_dict, f)
```

