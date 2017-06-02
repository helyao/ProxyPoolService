# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Filename:   getFreeProxy.py
    Author:     Helyao
    Description:
        Claw proxies from free proxy website
-------------------------------------------------
    Free proxy source supported:
        kuaidaili => http://www.kuaidaili.com/
-------------------------------------------------
    Change Logs:
    2017-05-26 8:48pm   create
-------------------------------------------------
"""
import lxml.html

from store.operRedis import RedisOperater
from util.utilFunction import download


class ProxyClawer:

    def __init__(self):
        self.roper = RedisOperater()

    def proxyKuai(self):
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


# Claw every free proxy source supported
def run():
    clawer = ProxyClawer()
    # get proxy from kuaidaili page 1 ~ 10
    clawer.proxyKuai()

if __name__ == '__main__':
    run()
    # overtime test
    # download('http://github.com', timeout=0.001)