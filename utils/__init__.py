#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/23 11:52 上午
# @Author : zhenyu lei
# @File : __init__.py.py
# @desc : 第三方工具类

def singleton(cls):

    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton()
