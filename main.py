#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/9 6:09 下午
# @Author : zhenyu lei
# @File : main.py
# @desc : 启动文件
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.gen

from handlers.example import example_handlers
from handlers.example.models import User
from manage import DefaultManager


def make_app():
    handlers = example_handlers
    return tornado.web.Application(handlers)


def main():
    """启动服务"""
    app = make_app()
    # app.listen(8000)
    service = tornado.httpserver.HTTPServer(app)
    service.bind(8000)
    service.start(1)
    tornado.ioloop.IOLoop.current().start()
    register_manager(app)


def register_manager(app: tornado.web.Application) -> None:
    """注册manager"""
    app.default_object = DefaultManager()  # 通过manager管理模型，可以注册多个manager


def create_tables() -> None:
    """表迁移
    Model.create_table
    """
    models = [User]
    [model.create_table() for model in models]


if __name__ == '__main__':
    main()
