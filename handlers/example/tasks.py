#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/26 3:27 下午
# @Author : zhenyu lei
# @File : tasks.py.py
# @desc : celery 任务队列
from celery import Celery

from libs.json_log_format import JsonLog
from tornado.concurrent import run_on_executor

broker = "redis://localhost:6379/1"
backend = "redis://localhost:6379/2"
app = Celery("test_tasks", broker=broker, backend=backend)


@app.task
def add_task():
    JsonLog.error()
