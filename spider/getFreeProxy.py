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
# import lxml
from clawer import download

class ProxyClawer:

    def __init__(self):
        pass

    def proxyKuai(self):
        for page in range(1, 11):
            url = 'http://www.kuaidaili.com/proxylist/{page}/'.format(page=page)
            html = download(url)


# Claw every free proxy source supported
def run():
    clawer = ProxyClawer()
    clawer.proxyKuai()

if __name__ == '__main__':
    # run()
    download('http://github.com', timeout=0.001)