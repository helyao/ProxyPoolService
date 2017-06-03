# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Filename:   xiciProxyApi.py
    Author:     Helyao
    Description:
        Get dynamic proxies list by xici-api.
-------------------------------------------------
    XiciDaili.com support free proxies by api
        HOST:   http://www.xicidaili.com/
        API:    http://api.xicidaili.com/free2016.txt
        This api updates every 15-minutes.
-------------------------------------------------
    Change Logs:
    2017-06-02 10:32am   create
-------------------------------------------------
"""
import os
import time
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

import sys
sys.path.append('..')

from store.operRedis import RedisOperater
from util.utilFunction import validUsefulProxy, download

XICI_API_URL = 'http://api.xicidaili.com/free2016.txt'

class xiciFreeApi():

    def __init__(self):
        self.all_proxies = []
        self.vaild_proxies = []
        self.invalid_proxies = []
        self.roper = RedisOperater()
        list = download(XICI_API_URL)
        self.all_proxies = list.split('\r\n')
        self._proxyFilter()
        self._getFilterReport()

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
    print('XiciDaili Task! The time is: {}'.format(datetime.now()))
    xici = xiciFreeApi()

def run():
    _task()
    scheduler = BlockingScheduler()
    scheduler.add_job(_task, 'interval', seconds=900)
    print('Press Ctrl+{} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

def _tick():
    time.sleep(2)
    print('Tick! The time is: {}'.format(datetime.now()))

def _scheduleTest():
    scheduler = BlockingScheduler()
    scheduler.add_job(_tick, 'interval', seconds=3)
    print('Press Ctrl+{} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

if __name__ == '__main__':
    # scheduleTest()
    run()
