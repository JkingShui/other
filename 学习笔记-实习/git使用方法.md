## 第一次使用时，先克隆，在配置信息

1. 配置公钥  https://blog.csdn.net/plei_yue/article/details/78959525
2. 在github创建仓库(文件夹)
3. git clone 路径         克隆到本地
4. git config --global user.email xxxxxx@xxxx.com          设置邮箱
5. git config --global user.name xxxxxxxxx                     设置name   邮箱和name对了 才会“绿”

## 提交文件

git pull   同步

git add xxx    添加到缓存

git status   查看状态

git commit -m "学习日记 2019.3.22"    添加备注，提到本地库

git push origin master      提交远程库

## 创建分支

git checkout -b feature-branch //创建并切换到分支feature-branch 

git push origin feature-branch:feature-branch //推送本地的feature-branch(冒号前面的)分支到远程origin的feature-branch(冒号后面的)分支(没有会自动创建)

## 删除文件

有两种方法

> 1、git rm xxxxxx      输出远端xxxx文件
>
> 
>
> 2、 rm xxx         删除本地文件
>
> git commit -m "xxx"
>
> git push origin master