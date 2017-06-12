# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Filename:   usUsableProxyHandler.py
    Author:     Helyao
    Description:
        Verify usable us-proxies
-------------------------------------------------
    Change Logs:
    2017-06-11  9:35pm  create
-------------------------------------------------
"""
import os
import time

import sys
sys.path.append('..')

from store.operRedis import UsRedisOperater
from util.utilFunction import validUsefulProxy

class ProxyUsUsableFilter():
    def __init__(self):
        self.roper = UsRedisOperater()

    def _handler(self):
        try:
            num = self.roper.getWorkinNum()
            if (num > 0):
                proxy = self.roper.getRandomUsable()
                print(proxy)
                num_retries = 3
                for i in range(0, num_retries):
                    if validUsefulProxy(proxy, mode='out'):
                        if (num <= 3):
                            time.sleep(3)
                        return
                self.roper.remWorkin(proxy)
            else:
                time.sleep(1)
        except Exception as ex:
            time.sleep(1)

    def run(self):
        print('Press Ctrl+{} to exit'.format('Break' if os.name == 'nt' else 'C'))
        while True:
            self._handler()

def run():
    pfilter = ProxyUsUsableFilter()
    pfilter.run()

if __name__ == '__main__':
    run()
