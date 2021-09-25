#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/25 9:55 上午
# @Author : zhenyu lei
# @File : config.py.py
# @desc : 获取配置文件
import configparser


class Config(object):

    conf = configparser.ConfigParser()  # 项目启动时初始化一次，直接使用类变量，共享全局变量（类）
    conf.read('../config.ini')


if __name__ == '__main__':
    Config.conf.add_section('OSS')
    Config.conf.set('OSS', 'bucket_name', 'leizhenyu')
    print(Config.conf.sections())
    print(dict(Config.conf['OSS']))
