#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/23 11:52 上午
# @Author : zhenyu lei
# @File : cache.py
# @desc : 缓存类
import aioredis


class Cache(object):

    cache = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Cache, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self._load_redis()

    def _load_redis(self):
        pool = aioredis.ConnectionPool.from_url('redis://localhost:6379/0',
                                                      max_connections=10)
        self.cache = aioredis.Redis(connection_pool=pool)


if __name__ == '__main__':
    async def main():
        redis = Cache()
        print(id(redis))
        await redis.cache.set('my-key', 'hahahaha')
        val = await redis.cache.get('my-key')
        print(val)
        await redis.cache.close()

    async def main2():
        redis = Cache()
        print(id(redis))
        val = await redis.cache.get('my-key')
        print(val)
        await redis.cache.close()
    import asyncio
    asyncio.run(main())
    asyncio.run(main2())
