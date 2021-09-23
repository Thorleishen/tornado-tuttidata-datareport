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


class TestCaseRequest(tornado.web.RequestHandler):

    def _initialize(self) -> None:
        pass

    def prepare(self):
        """进入request handler 之前的操作"""

    def on_finish(self) -> None:
        """结束request handler操作"""

    @tornado.web.asynchronous
    def get(self):
        params = self.get_arguments()


def make_app():
    handlers = []
    return tornado.web.Application(handlers)


if __name__ == '__main__':
    app = make_app()
    # app.listen(8000)
    service = tornado.httpserver.HTTPServer(app)
    service.bind(8000)
    service.start(4)
    tornado.ioloop.IOLoop.current().start()
