#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/25 11:42 上午
# @Author : zhenyu lei
# @File : json_log_format.py
# @desc : 日志处理
import logging
import time


class JsonLog(object):

    _instance = {}  # 单例模式

    def __new__(cls, filename: str = 'test', *args, **kwargs):
        if filename not in cls._instance:
            cls._instance[filename] = super(JsonLog, cls).__new__(cls, *args, **kwargs)
        return cls._instance[filename]

    def __init__(self, filename: str):
        logging.basicConfig(filename=f'../logs/{filename}-{time.strftime("%Y-%m-%d", time.localtime())}.log',
                            format="%(message)s")
        self.logger = logging.getLogger()

    def debug(self, error_code=None, msg=None, order_no=None, data=None, exception=None):
        level = 'DEBUG'
        self.logger.debug('test')

    def info(self, error_code=None, msg=None, order_no=None, data=None, exception=None):
        level = 'INFO'

    def warning(self, error_code=None, msg=None, order_no=None, data=None, exception=None):
        level = 'WARNING'

    def error(self, error_code=None, msg=None, order_no=None, data=None, exception=None):
        level = 'ERROR'
        self.logger.error('test')


if __name__ == '__main__':
    log = JsonLog('test')
    log.error()
