#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/23 4:12 下午
# @Author : zhenyu lei
# @File : mongo_client.py
# @desc : MongoDB连接 - motor
import motor
from motor.core import AgnosticCollection

from libs.config import Config
from utils import singleton


@singleton
class MongoDBClient(object):

    def __init__(self, collection_name: str, client: motor.motor_tornado.MotorClient = None, collection: AgnosticCollection = None):
        self.mongo_conf = dict(Config.conf['MONGO'])
        self.collection_name = collection_name
        self.client = client
        self.collection = collection
        self._create_client()

    def _create_client(self):
        self.client = motor.motor_tornado.MotorClient(self.mongo_conf['mongo_url'] or 'mongodb://localhost:27017')
        self.collection = self.client[self.collection_name]


if __name__ == '__main__':
    async def main():
        client = MongoDBClient('test')
        await client.collection.find_one({'i': {'$lt': 1}})
