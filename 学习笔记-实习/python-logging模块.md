## 日志的重要性

在开发过程中，如果程序运行出现了问题，我们是可以使用Debug工具来检测到到底是哪一步出现了问题，如果出现了问题的话，是很容易排查的。但是到生产环境中，这时候代码相当于是在一个黑盒环境下运行的，我们只能看到其运行的效果，是不能直接看到代码运行过程中每一步的状态的。所有日志很重要

## 日志记录的流程框架

![img](https://user-gold-cdn.xitu.io/2018/6/3/163c618941cfc03f?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

+ Logger：即 Logger Main Class，是我们进行日志记录时创建的对象，我们可以调用它的方法传入日志模板和信息，来生成一条条日志记录，称作 Log Record。

- Log Record：就代指生成的一条条日志记录。
- Handler：即用来处理日志记录的类，它可以将 Log Record 输出到我们指定的日志位置和存储形式等，如我们可以指定将日志通过 FTP 协议记录到远程的服务器上，Handler 就会帮我们完成这些事情。
- Formatter：实际上生成的 Log Record 也是一个个对象，那么我们想要把它们保存成一条条我们想要的日志文本的话，就需要有一个格式化的过程，那么这个过程就由 Formatter 来完成，返回的就是日志字符串，然后传回给 Handler 来处理。
- Filter：另外保存日志的时候我们可能不需要全部保存，我们可能只需要保存我们想要的部分就可以了，所以保存前还需要进行一下过滤，留下我们想要的日志，如只保存某个级别的日志，或只保存包含某个关键字的日志等，那么这个过滤过程就交给 Filter 来完成。
- Parent Handler：Handler 之间可以存在分层关系，以使得不同 Handler 之间共享相同功能的代码。

以上就是整个 logging 模块的基本架构和对象功能，了解了之后我们详细来了解一下 logging 模块的用法。

```python
import logging  #导入logging模块

 # basicConfig 配置了 level 信息和 format 信息
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')   
logger = logging.getLogger(__name__) #声明一个logger对象， __name__当前文件的名称

logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')
```

**运行结果：**

![1553841313914](C:\Users\sangfor\AppData\Roaming\Typora\typora-user-images\1553841313914.png)

我们在代码中将输出级别（level）设置为INFO，可以看出，DEBUG的信息没有被打印，这样在实际环境中，会过滤掉数量多而且用处不大的DEBUG信息

下面介绍一下basicConfig函数可传入的参数

- filename：即日志输出的文件名，如果指定了这个信息之后，实际上会启用 FileHandler，而不再是 StreamHandler，这样日志信息便会输出到文件中了。

- filemode：这个是指定日志文件的写入方式，有两种形式，一种是 w，一种是 a，分别代表清除后写入和追加写入。

- format：指定日志信息的输出格式，即上文示例所示的参数，部分参数可以参考：

  - %(levelno)s：打印日志级别的数值。
  - %(levelname)s：打印日志级别的名称。
  - %(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]。
  - %(filename)s：打印当前执行程序名。
  - %(funcName)s：打印日志的当前函数。
  - %(lineno)d：打印日志的当前行号。
  - %(asctime)s：打印日志的时间。
  - %(thread)d：打印线程ID。
  - %(threadName)s：打印线程名称。
  - %(process)d：打印进程ID。
  - %(processName)s：打印线程名称。
  - %(module)s：打印模块名称。
  - %(message)s：打印日志信息。

- datefmt：指定时间的输出格式。

- style：如果 format 参数指定了，这个参数就可以指定格式化时的占位符风格，如 %、{、$ 等。

- level：指定日志输出的类别，程序会输出大于等于此级别的信息。

- stream：在没有指定 filename 的时候会默认使用 StreamHandler，这时 stream 可以指定初始化的文件流。

- handlers：可以指定日志处理时所使用的 Handlers，必须是可迭代的。

  ```python
  import  logging  #引入了 logging 模块
  logging.basicConfig(
      level=logging.DEBUG,
      datefmt='%Y/%m/%d - %H:%M:%S',
      format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s',
      filename='test.log') #进行了一下基本的配置，
  logger = logging.getLogger(__name__) #创建一个logger
  
  logger.info('This is a log info')
  logger.debug('Debugging')
  logger.warning('Warning exists')
  logger.info('Finish')
  ```

  **输出结果：**

![1553843124744](C:\Users\sangfor\AppData\Roaming\Typora\typora-user-images\1553843124744.png)

## Level

设置了level之后只会记录（保存）level以上的信息，具体对应的数值如下：

![1553843295188](C:\Users\sangfor\AppData\Roaming\Typora\typora-user-images\1553843295188.png)



## Handler

basicConfig 是一个全局的”格式“设置，但在一个工程中不可能所有的日志个是都是一样的，为了灵活可以考虑使用handler，看看下面实例：

```python
import logging

# 声明了一个 Logger 对象
logger = logging.getLogger(__name__) 
# 设置输出等级
logger.setLevel(level=logging.INFO)  
# 指定了其对应的 Handler 为 FileHandler 对象
handler = logging.FileHandler('output.log') 
# Handler 对象还单独指定了 Formatter 对象单独配置输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# 最后给 Logger 对象添加对应的 Handler 
logger.addHandler(handler)

logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')
```

首先创建了一个logger对象，然后对这个特定的logger进行设置，然后用这个logger进行日志输出

> 另外我们还可以使用其他的 Handler 进行日志的输出，logging 模块提供的 Handler 有：

- StreamHandler：logging.StreamHandler；日志输出到流，可以是 sys.stderr，sys.stdout 或者文件。
- FileHandler：logging.FileHandler；日志输出到文件。
- BaseRotatingHandler：logging.handlers.BaseRotatingHandler；基本的日志回滚方式。
- RotatingHandler：logging.handlers.RotatingHandler；日志回滚方式，支持日志文件最大数量和日志文件回滚。
- TimeRotatingHandler：logging.handlers.TimeRotatingHandler；日志回滚方式，在一定时间区域内回滚日志文件。
- SocketHandler：logging.handlers.SocketHandler；远程输出日志到TCP/IP sockets。
- DatagramHandler：logging.handlers.DatagramHandler；远程输出日志到UDP sockets。
- SMTPHandler：logging.handlers.SMTPHandler；远程输出日志到邮件地址。
- SysLogHandler：logging.handlers.SysLogHandler；日志输出到syslog。
- NTEventLogHandler：logging.handlers.NTEventLogHandler；远程输出日志到Windows NT/2000/XP的事件日志。
- MemoryHandler：logging.handlers.MemoryHandler；日志输出到内存中的指定buffer。
- HTTPHandler：logging.handlers.HTTPHandler；通过”GET”或者”POST”远程输出到HTTP服务器。



## Formatter

在进行日志格式化输出的时候，我们可以不借助于 basicConfig 来全局配置格式化输出内容，可以借助于 Formatter 来完成，下面我们再来单独看下 Formatter 的用法，看Handler代码。

## 捕获Traceback

如果遇到错误，我们更希望报错时出现的详细 Traceback 信息，便于调试，利用 logging 模块我们可以非常方便地实现这个记录

```python
import  logging  #引入了 logging 模块
logging.basicConfig(
    level=logging.DEBUG,
    datefmt='%Y/%m/%d - %H:%M:%S',
    format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s',
    filename='test.log') #进行了一下基本的配置，
logger = logging.getLogger(__name__) #创建一个logger

try:
    res = 10 /0
except Exception:
    logger.error('faild to get result!', exc_info=True)
logging.info('fineshed')
```

**输出结果：**

![1553845366145](C:\Users\sangfor\AppData\Roaming\Typora\typora-user-images\1553845366145.png)