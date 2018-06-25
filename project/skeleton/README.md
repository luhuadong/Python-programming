# 项目骨架

　　skeleton 是一个项目“骨架”目录，这个骨架目录具备让项目跑起来的所有基本内容。其中包含项目文件布局、自动化测试代码、模组以及安装脚本。当您建立一个新项目的时候，只要把这个目录复制过去，修改目录的名字，再编辑里面的文件即可。

　　skeleton 目录是新项目的基础目录，其中的 NAME 目录是您的项目主目录，当您使用这个骨架的时候，可以将它修改为您想要的名字。

　　您需要修改 setup.py 文件，将项目信息和联系方式填写进去。

　　tests/NAME_tests.py 是一个简单的测试专用的骨架文件。

--------

# 安装软件包

　　通常，你需要安装以下软件包：

- pip —— http://pypi.python.org/pypi/pip
- distribute —— http://pypi.python.org/pypi/distribute
- nose —— http://pypi.python.org/pypi/nose
- virtualenv —— http://pypi.python.org/pypi/virtualenv

--------

# 测试

　　安装上述软件包后，可以使用 nosetests 进行测试。
　　如果尚未安装 nosetests，在 Ubuntu 上可以执行命令安装：

```
sudo apt-get install python-nose
```

　　然后在 skeleton 目录中运行 `nosetests`，如果看到如下画面，则说明配置成功。

```
$ nosetests
.
----------------------------------------------------------------------
Ran 1 test in 0.002s

OK
```

--------

# 使用这个骨架

　　以后每次新建项目时，只要做下面的事情就可以了：

1. 拷贝这份 skeleton 目录，把名字改成新项目的名字；
2. 再将 NAME 模组更名为你需要的名字，它可以是你项目的名字，也可以是你喜欢的任意名字；
3. 编辑 setup.py 让它包含你新项目的相关信息；
4. 重命名 tests/NAME_tests.py，让它的名字匹配到你模组的名字；
5. 使用 nosetests 检查有无错误；
6. 开始写代码吧。

