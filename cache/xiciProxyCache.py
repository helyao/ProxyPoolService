# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Filename:   xiciProxyCache.py
    Author:     Helyao
    Description:
        Cache xicidaili to local file
-------------------------------------------------
    KuaiDaili free proxy source supported:
        kuaidaili => http://www.xicidaili.com/
-------------------------------------------------
    Change Logs:
    2017-07-07  3:44pm     create
-------------------------------------------------
"""
import os
import time
import lxml.html
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

import sys
sys.path.append('..')

from store.operRedis import RedisOperater
from util.utilFunction import download2

KUQI_SRC_BASE_URL = 'http://www.xicidaili.com/'

class xiciProxyDownload():
    def __init__(self):
        self.roper = RedisOperater()
        self._crawler()

    def _crawler(self):
        for page in range(1, 100):
            try:
                url = 'http://www.xicidaili.com/nn/{page}'.format(page=page)
                html = download2(url)
                filename = 'xici{}.list'.format(page)
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(html)
                time.sleep(10)
            except Exception as ex:
                print(ex)
        for page in range(1, 100):
            try:
                url = 'http://www.xicidaili.com/nt/{page}'.format(page=page)
                html = download2(url)
                filename = 'xici{}.list'.format(page+100)
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(html)
                time.sleep(10)
            except Exception as ex:
                print(ex)

def run():
    crawler = xiciProxyDownload()


if __name__ == '__main__':
    run()