# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Filename:   blobProxyApi.py
    Author:     Helyao
    Description:
        Get free proxies from jsonblob api.
-------------------------------------------------
    jsonblob.com support free proxies by api
        API:    https://jsonblob.com/api/jsonBlob/31bf2dc8-00e6-11e7-a0ba-e39b7fdbe78b
        This is a static file, just run once to check the proxies usability.
-------------------------------------------------
    Change Logs:
    2017-06-07  6:45am  create
    2017-06-09  4:02pm  always loop
-------------------------------------------------
"""
import re
import os
import time
from datetime import datetime

import sys
sys.path.append('..')

from store.operRedis import RedisOperater
from util.utilFunction import validUsefulProxy, download
from apscheduler.schedulers.blocking import BlockingScheduler

BLOB_API_URL = 'https://jsonblob.com/api/jsonBlob/31bf2dc8-00e6-11e7-a0ba-e39b7fdbe78b'

class blobFreeApi():
    def __init__(self):
        self.all_proxies = []
        self.vaild_proxies = []
        self.invalid_proxies = []
        self.roper = RedisOperater()
        content = download(BLOB_API_URL)
        self.all_proxies = re.findall(r'\d+.\d+.\d+.\d+:\d+', content)
        self._proxyFilter()

    def _proxyFilter(self):
        for item in self.all_proxies:
            if validUsefulProxy(item):
                self.vaild_proxies.append(item)
                self.roper.addworkin(item)
            else:
                self.invalid_proxies.append(item)

    def _getFilterReport(self):
        print('The length of all proxies array is {}'.format(len(self.all_proxies)))
        print('And valid proxies array is {}'.format(len(self.vaild_proxies)))
        print(self.vaild_proxies)
        print('And invalid proxies array is {}'.format(len(self.invalid_proxies)))


def _task():
    blob = blobFreeApi()
    blob._getFilterReport()

def runWithSchedule():
    _task()
    scheduler = BlockingScheduler()
    scheduler.add_job(_task, 'interval', seconds=10000)
    print('Press Ctrl+{} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

def run():
    while True:
        _task()

if __name__ == '__main__':
    run()

