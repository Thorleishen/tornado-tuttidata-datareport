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


def make_app():
    handlers = example_handlers
    return tornado.web.Application(handlers)


if __name__ == '__main__':
    app = make_app()
    # app.listen(8000)
    service = tornado.httpserver.HTTPServer(app)
    service.bind(8000)
    service.start(1)
    tornado.ioloop.IOLoop.current().start()
