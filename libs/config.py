#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/25 9:55 上午
# @Author : zhenyu lei
# @File : config.py.py
# @desc : 获取配置文件
import configparser

from utils import singleton


@singleton
class Config(object):

    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read('../config.ini')
        self.setions = self.conf.sections()
