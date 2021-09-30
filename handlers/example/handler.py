#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/26 3:35 下午
# @Author : zhenyu lei
# @File : handler.py
# @desc : RequestHandler 类
import tornado.web
from tornado.gen import coroutine
import tornado.concurrent
import asyncio
import tornado.ioloop

from handlers.example.tasks import add_task


class TestHandler(tornado.web.RequestHandler):

    async def get(self):
        # TODO celery是同步，使用 apply_async放入队列中，让worker消费，如果apply_async耗时的话那么就应该考虑rabbitmq的连接这块
        add_task.apply_async()  # 使用celery apply_async/delay 异步执行任务即添加到队列中通过celery worker 执行任务
        self.finish('test')

    async def post(self):
        ioloop = tornado.ioloop.IOLoop.current()
        ioloop.add_handler()
