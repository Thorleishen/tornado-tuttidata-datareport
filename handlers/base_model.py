#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/30 3:03 下午
# @Author : zhenyu lei
# @File : base_model.py
# @desc : 模型基类
from peewee import Model

from libs.mysql_client import MySQLClientPool


class BaseModel(Model):
    """A base model that will use our MySQL Poll database"""

    class Meta:
        database = MySQLClientPool('default').database
