# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Filename:   operRedis.py
    Author:     Helyao
    Description:
        Support redis operations for data storage
-------------------------------------------------
    Change Logs:
    2017-06-01 5:27pm   create
-------------------------------------------------
"""

import redis
import configparser
from config import CONFIG_INI

class RedisOperater():
    def __init__(self):
        try:
            cp = configparser.ConfigParser()
            cp.read(CONFIG_INI)
            host = cp.get('redis', 'host')
            port = cp.getint('redis', 'port')
            db = cp.getint('redis', 'db')
            self.cachename = cp.get('redis', 'cache')
            self.workinname = cp.get('redis', 'workin')
            print('Redis Connection: {host}:{port}/{db}?cache={cache}&workin={workin}'.format(host=host, port=port, db=db, cache=self.cachename, workin=self.workinname))
            rconn = redis.ConnectionPool(host=host, port=port, db=db)
            self.rdb = redis.Redis(connection_pool=rconn)
        except Exception as ex:
            print('[operRedis]: {}'.format(ex))

    def addcache(self, str):
        self.rdb.sadd(self.cachename, str)

    def addworkin(self, str):
        self.rdb.sadd(self.workinname, str)

    def getRandomUsable(self):
        if self.rdb.scard(self.workinname):
            return self.rdb.srandmember(self.workinname, 1)[0].decode('utf-8')
        else:
            return

    @staticmethod
    def redisConnectUnitTest(rdb):
        # add url string in set
        rdb.sadd('set_test', '127.0.0.1:8080')
        rdb.sadd('set_test', '0.0.0.0:8000')
        rdb.sadd('set_test', '0.0.0.0:8000')
        # get all members in set
        print('smember all data in set_test, the number = {}'.format(rdb.scard('set_test')))
        urlist = rdb.smembers('set_test')
        for url in urlist:
            print(url.decode('utf-8'))
        # judge '0.0.0.0:8000' in set (return null)
        if rdb.sismember('set_test', '0.0.0.0:8000'):
            print('found 0.0.0.0:8000')
        else:
            print('0.0.0.0:8000 is deleted')
        # delete set_test
        rdb.flushdb()

    def _test(self):
        self.redisConnectUnitTest(self.rdb)

if __name__ == '__main__':
    roper = RedisOperater()
    # roper._test()
    print(roper.getRandomUsable())
