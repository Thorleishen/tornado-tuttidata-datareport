''#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/27 6:12 下午
# @Author : zhenyu lei
# @File : DataUploadMiddleWare.py
# @desc : 数据上传中间键
from middleware.middleware import BaseMiddleWare


class Md5SignMiddleWare(BaseMiddleWare):

    def get_current_user(self):
        """md5 校验
        secret 加盐加密
        """
