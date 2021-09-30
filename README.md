# tornado-tuttidata-datareport
基于tornado - celery 数据上报 - 项目结构

tornado + peewee + peewee-async + aiomysql + motor + \
tornado-celery: https://gitee.com/yohannlee/tornado-celery/blob/master/examples/tornado_async.py


## 文件目录结构
.
├── README.md
├── default.config.ini
├── handlers
│   ├── __init__.py
│   ├── __pycache__
│   │   └── __init__.cpython-37.pyc
│   ├── base_model.py
│   └── example
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-37.pyc
│       │   ├── handler.cpython-37.pyc
│       │   └── tasks.cpython-37.pyc
│       ├── handler.py
│       ├── models.py
│       └── tasks.py
├── libs
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   └── json_log_format.cpython-37.pyc
│   ├── cache.py
│   ├── config.py
│   ├── json_log_format.py
│   ├── mongo_client.py
│   └── mysql_client.py
├── logs
│   ├── log.txt
│   └── test-2021-09-25.log
├── main.py
├── manage.py
├── middleware
│   ├── DataUploadMiddleWare.py
│   ├── JwtTokenMiddleWare.py
│   ├── __init__.py
│   └── middleware.py
├── models
│   └── __init__.py
├── requirment.txt
├── static
│   ├── css
│   │   └── test.css
│   ├── image
│   │   └── a.jpg
│   └── js
│       └── test.js
├── templates
│   └── test.html
└── utils
    ├── __init__.py
    └── __pycache__
        └── __init__.cpython-37.pyc

- handlers 
    按模块区分RequestHandler
- libs
    第三方库工具类 MySQL Redis Mongo configparser Log
- logs
    日志存储目录 - 按日期存储
- middleware 
    中间件
- models
    model 模型处理类，用于增删改查
- static 
    静态文件 js css img
- templates 
    mvt 模版
- utils 
    通用工具类
- manage.py
    model模型管理
- main.py
    服务启动主函数
- requirment.txt
    依赖包
    
> main 函数 对router注册，manage注册以及表迁移做处理
> middleware 通用中间件，实现中间层数据处理以及服务接口耗时等日志信息


### 功能
目前只是对以往项目结构进行重构，以及通用功能进行封装
