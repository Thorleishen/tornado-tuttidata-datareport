#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/30 2:08 下午
# @Author : zhenyu lei
# @File : mysql_client.py
# @desc : 数据库连接池 - peewee_async
from os import cpu_count

from peewee_async import PooledMySQLDatabase

from libs.config import Config


class MySQLClientPool(object):

    max_connections = cpu_count() * 2 + 1  # 默认是cpu核心数*2加1
    _instance = {}  # 针对不同的数据库做处理

    def __new__(cls, database, *args, **kwargs):
        if database not in cls._instance:
            cls._instance[database] = super(MySQLClientPool, cls).__new__(cls, *args, **kwargs)
        return cls._instance[database]

    def __init__(self, database, mysql_conf=None):
        mysql_conf = mysql_conf or dict(Config.conf['MYSQL'])
        self.database = PooledMySQLDatabase(database, user=mysql_conf['username'],
                                            password=mysql_conf['password'], host=mysql_conf['host'],
                                            port=mysql_conf['port'])

