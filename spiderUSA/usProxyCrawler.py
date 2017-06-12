# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Filename:   usProxyCrawler.py
    Author:     Helyao
    Description:
        Get proxies from us-proxy website..
-------------------------------------------------
    us-proxy free proxy source supported:
        us-proxy => https://www.us-proxy.org/
-------------------------------------------------
    Change Logs:
    2017-06-11  7:39pm  create
-------------------------------------------------
"""

import os
import lxml.html
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

import sys
sys.path.append('..')

from store.operRedis import UsRedisOperater
from util.utilFunction import download

US_SRC_BASE_URL = 'https://www.us-proxy.org/'

class usFreeCrawler():
    def __init__(self):
        self.roper = UsRedisOperater()
        self._crawler()

    def _crawler(self):
        try:
            html = download(US_SRC_BASE_URL)
            tree = lxml.html.fromstring(html)
            content = tree.xpath('//table/tbody/tr/td/text()')
            for item in range(0, int(len(content) / 8)):
                ip = content[item * 8]
                port = content[item * 8 + 1]
                self.roper.addCache('{ip}:{port}'.format(ip=ip, port=port))
            print('Get {num} us-proxies'.format(num=int(len(content)/8)))
        except Exception as ex:
            print(ex)

def _task():
    print('Us-Proxy Task! The time is: {}'.format(datetime.now()))
    crawler = usFreeCrawler()

def run():
    _task()
    scheduler = BlockingScheduler()
    scheduler.add_job(_task, 'interval', seconds=1800)
    print('Press Ctrl+{} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

if __name__ == '__main__':
    run()

