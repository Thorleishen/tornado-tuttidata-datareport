#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/26 4:12 下午
# @Author : zhenyu lei
# @File : models.py
# @desc :
from peewee import CharField

from handlers.base_model import BaseModel


class User(BaseModel):
    username = CharField()

    class Meta:
        table_name = 'user'
