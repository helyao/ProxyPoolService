# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Filename:   usableProxyHandler.py
    Author:     Helyao
    Description:
        Verify usable proxies
-------------------------------------------------
    Change Logs:
    2017-06-01 7:04pm   create
-------------------------------------------------
"""
import os
import time
import redis
import configparser

import sys
sys.path.append('..')

from config import CONFIG_INI
from util.utilFunction import validUsefulProxy

class ProxyUsableFilter():
    def __init__(self):
        try:
            cp = configparser.ConfigParser()
            cp.read(CONFIG_INI)
            host = cp.get('redis', 'host')
            port = cp.getint('redis', 'port')
            db = cp.getint('redis', 'db')
            self.cachename = cp.get('redis', 'cache')
            self.workinname = cp.get('redis', 'workin')
            print('Redis Connection: {host}:{port}/{db} cache = {cache} & workin = {workin}'.format(host=host, port=port, db=db, cache=self.cachename, workin=self.workinname))
            rconn = redis.ConnectionPool(host=host, port=port, db=db)
            self.rdb = redis.Redis(connection_pool=rconn)
        except Exception as ex:
            print('[operRedis]: {}'.format(ex))

    def _handler(self):
        try:
            proxy = self.rdb.srandmember(self.workinname, 1)[0].decode('utf-8')
            num_retries = 3
            for i in range(0, num_retries):
                if validUsefulProxy(proxy):
                    return
            self.rdb.srem(self.workinname, proxy)
        except Exception as ex:
            time.sleep(2)

    def run(self):
        print('Press Ctrl+{} to exit'.format('Break' if os.name == 'nt' else 'C'))
        while True:
            self._handler()

def run():
    pfilter = ProxyUsableFilter()
    pfilter.run()

if __name__ == '__main__':
    run()
