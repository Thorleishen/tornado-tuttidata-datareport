#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/25 3:31 下午
# @Author : zhenyu lei
# @File : middleware.py
# @desc : 通用中间件
import time
from abc import ABC

import tornado.web
import tornado.gen


class BaseMiddleWare(tornado.web.RequestHandler):

    def initialize(self, *args, **kwargs):
        """此方法用于初始化实例变量, *args **kwargs 通过 application中传递"""
        pass

    def get_current_user(self):
        """用户身份校验 @tornado.web.authenticated """
        pass

    def set_default_headers(self) -> None:
        """设置默认headers 也可在nginx代理中配置跨域问题
        浏览器发送第一次option请求检测是否允许跨域
        """
        self.set_header('Access-Control-Allow-Origin', '*')  # * 表示允许所有的域名通过
        self.set_header('Access-Control-Allow-Credentials', 'true')
        self.set_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')  # 设置允许哪些请求方式可通过
        self.set_header('Access-Control-Allow-Headers',
                        'DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range')
        self.set_header('Access-Control-Expose-Headers', 'Content-Length,Content-Range')
        self.set_header('Access-Control-Max-Age', '3600')

    def prepare(self):
        """在调用 get/post/header/option 方法前使用"""
        self.start_time = time.time()

    def on_finish(self):
        """请求结束时使用"""
        self.duration = time.time() - self.start_time  # 接口耗时

    async def options(self):
        self.finish()
