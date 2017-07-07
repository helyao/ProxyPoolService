# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Filename:   xiciProxyCrawler.py
    Author:     Helyao
    Description:
        Add to proxy pool from static xici html buffer
-------------------------------------------------
    KuaiDaili free proxy source supported:
        kuaidaili => http://www.xicidaili.com/
-------------------------------------------------
    Change Logs:
    2017-07-07  03:55pm     create
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

class xiciStaticProxy():
    def __init__(self):
        self.roper = RedisOperater()
        self._crawler()

    def _crawler(self):
        for page in range(1, 20):
            try:
                filename = 'xici/xici{}.list'.format(page)
                with open(filename, 'r', encoding='utf-8') as f:
                    html = f.read()
                    tree = lxml.html.fromstring(html)
                    tds = tree.cssselect('td')
                    count = int(len(tds) / 10)
                    print(count)
                    for line in range(0, count):
                        ip = tds[line * 10 + 1].text
                        port = tds[line * 10 + 2].text
                        proxy = '{ip}:{port}'.format(ip=ip, port=port)
                        print(proxy)
                        self.roper.addcache(proxy)
                time.sleep(10)
            except Exception as ex:
                print(ex)

def _task():
    print('XiciDaili Task! The time is: {}'.format(datetime.now()))
    crawler = xiciStaticProxy()

def run():
    _task()
    scheduler = BlockingScheduler()
    scheduler.add_job(_task, 'interval', seconds=3000)
    print('Press Ctrl+{} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

if __name__ == '__main__':
    run()