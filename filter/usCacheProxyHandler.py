# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Filename:   usCacheProxyHandler.py
    Author:     Helyao
    Description:
        Judge cache proxies with out-website
-------------------------------------------------
    Change Logs:
    2017-06-11  8:56pm  create
-------------------------------------------------
"""

import os
import time

import sys
sys.path.append('..')

from store.operRedis import UsRedisOperater
from util.utilFunction import validUsefulProxy

class ProxyUsCacheFilter():
    def __init__(self):
        self.roper = UsRedisOperater()

    def _handler(self):
        try:
            if (self.roper.getCacheNum() > 0):
                proxy = self.roper.getRandomUntrust()
                print(proxy)
                self.roper.remCache(proxy)
                if validUsefulProxy(proxy, mode='out'):
                    self.roper.addWorkin(proxy)
            else:
                time.sleep(1)
                return
        except Exception as ex:
            time.sleep(2)

    def run(self):
        print('Press Ctrl+{} to exit'.format('Break' if os.name == 'nt' else 'C'))
        while True:
            self._handler()

def run():
    pfilter = ProxyUsCacheFilter()
    pfilter.run()

if __name__ == '__main__':
    run()

