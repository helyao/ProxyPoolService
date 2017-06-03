# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Filename:   kuaiProxyClawer.py
    Author:     Helyao
    Description:
        Claw proxies from kuaidaili website..
-------------------------------------------------
    KuaiDaili free proxy source supported:
        kuaidaili => http://www.kuaidaili.com/
-------------------------------------------------
    Change Logs:
    2017-06-03 11:56am   create
-------------------------------------------------
"""
import os
import lxml.html
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

import sys
sys.path.append('..')

from store.operRedis import RedisOperater
from util.utilFunction import download

KUQI_SRC_BASE_URL = 'http://www.kuaidaili.com/'

class kuaiFreeClawer():
    def __init__(self):
        self.roper = RedisOperater()
        self._clawer()

    def _clawer(self):
        for page in range(1, 11):
            url = 'http://www.kuaidaili.com/proxylist/{page}/'.format(page=page)
            html = download(url)
            tree = lxml.html.fromstring(html)
            ips = tree.cssselect('td[data-title="IP"]')
            ports = tree.cssselect('td[data-title="PORT"]')
            for item in range(0, len(ips)):
                proxy = '{ip}:{port}'.format(ip=ips[item].text, port=ports[item].text)
                print(proxy)
                self.roper.addcache(proxy)

def _task():
    print('KuaiDaili Task! The time is: {}'.format(datetime.now()))
    clawer = kuaiFreeClawer()

def run():
    _task()
    scheduler = BlockingScheduler()
    scheduler.add_job(_task, 'interval', seconds=600)
    print('Press Ctrl+{} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

if __name__ == '__main__':
    run()