#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/25 3:54 下午
# @Author : zhenyu lei
# @File : JwtTokenMiddleWare.py
# @desc :
from middleware.middleware import BaseMiddleWare
import jwt


class JwtTokenMiddleWare(BaseMiddleWare):

    def get_current_user(self):
        token = self.get_argument('token', '')
        if not token:
            return False
        payload = JwtToken.auth_token(token)
        if not payload:
            return False
        return True


class JwtToken(object):

    secret_key = 'asd,,2021'

    def __init__(self):
        pass

    @classmethod
    def create_token(cls, payload: dict):
        """生成token 和 过期后自动生成新的token
        {'token_expire_time': 16132949234, 'expire_time': 17132949234}
        token_expire_time 生成token的过期时间，防止过期重刷
        expire_time 过期时间，类似于cookie的过期时间，重新登陆
        """
        token = jwt.encode(payload, cls.secret_key, algorithm='HS256')
        return token

    @classmethod
    def auth_token(cls, token):
        """JWT 解密"""
        payload = jwt.decode(token, cls.secret_key, algorithms=['HS256'])
        if not payload:
            return False
        return payload

