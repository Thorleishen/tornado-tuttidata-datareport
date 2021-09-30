#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/23 11:48 上午
# @Author : zhenyu lei
# @File : manage.py
# @desc : 命令注册
from peewee_async import Manager

from libs.mysql_client import MySQLClientPool


class DefaultManager(Manager):

    database = MySQLClientPool('default').database
