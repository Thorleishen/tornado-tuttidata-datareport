#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/26 3:35 下午
# @Author : zhenyu lei
# @File : handler.py
# @desc : RequestHandler 类
import tornado.web
from tornado.gen import coroutine

from handlers.example.tasks import add_task


class TestHandler(tornado.web.RequestHandler):

    async def get(self):
        add_task.apply_async()  # 使用celery apply_async/delay 异步执行任务即添加到队列中通过celery worker 执行任务
        self.finish('test')
