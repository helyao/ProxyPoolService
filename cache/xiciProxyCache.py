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
import requests

PAGE_NUM = 10

def download2(url, timeout=10, user_agent='wswp', num_retries=2):
    print('Downloading: {url}'.format(url=url))
    headers = {'User-agent': user_agent}
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        code = response.status_code
        if (num_retries > 0):
            if (500 <= code < 600):
                return download2(url, timeout, user_agent, num_retries-1)
        else:
            return None
        html = response.text
        return html
    except requests.ReadTimeout as ex:
        print('Download Timeout: {ex}'.format(ex=ex))
        return download2(url, timeout, user_agent, num_retries - 1)
    except Exception as ex:
        print('Download error: {ex}'.format(ex=ex))

class xiciProxyDownload():
    def __init__(self):
        self._crawler()

    def _crawler(self):
        for page in range(1, PAGE_NUM+1):
            try:
                url = 'http://www.xicidaili.com/nn/{page}'.format(page=page)
                html = download2(url)
                filename = 'xici{}.list'.format(page)
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(html)
                time.sleep(60)
            except Exception as ex:
                print(ex)
        for page in range(1, PAGE_NUM+1):
            try:
                url = 'http://www.xicidaili.com/nt/{page}'.format(page=page)
                html = download2(url)
                filename = 'xici{}.list'.format(page+PAGE_NUM)
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(html)
                time.sleep(60)
            except Exception as ex:
                print(ex)

def run():
    crawler = xiciProxyDownload()


if __name__ == '__main__':
    run()