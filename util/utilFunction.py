# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Filename:   utilFunction.py
    Author:     Helyao
    Description:
        Support base functions.
-------------------------------------------------
    Change Logs:
    2017-06-01 11:17pm   create
-------------------------------------------------
"""
import requests
from random import choice

import sys
sys.path.append('..')

from store.operRedis import RedisOperater

# TESTSIDE = ['https://www.baidu.com/', 'http://cn.bing.com/', 'https://www.sogou.com/', 'https://www.so.com/',
#             'https://www.douban.com/', 'http://www.sina.com.cn/', 'https://www.jd.com/', 'https://www.taobao.com/']
TESTSIDE = ['https://www.baidu.com/', 'https://www.jd.com/', 'https://www.taobao.com/']
TESTSIDE_US = ['https://www.google.com/', 'http://www.facebook.com/']
OVERTIME = 10

def validUsefulProxy(proxy, num_retries=2, mode='in'):
    # proxies = {protocol: "{protocol}://{proxy}".format(protocol=protocol, proxy=proxy)}
    proxies = {"http": "http://{proxy}".format(proxy=proxy), "https": "https://{proxy}".format(proxy=proxy)}
    try:
        if num_retries > 0:
            if mode=='in':
                url = choice(TESTSIDE)
            else:
                url = choice(TESTSIDE_US)
            print(url)
            res = requests.get(url, proxies=proxies, timeout=OVERTIME, verify=False)
            print(res.status_code)
            if res.status_code == 200:
                return True
            elif 500 <= res.status_code < 600:
                # retry 5XX HTTP errors
                if mode == 'in':
                    return validUsefulProxy(proxy, num_retries - 1, 'in')
                else:
                    return validUsefulProxy(proxy, num_retries - 1, 'out')
    except Exception as ex:
        print(ex)
        return False

def download(url, timeout=10, user_agent='wswp', num_retries=2):
    print('Downloading: {url}'.format(url=url))
    headers = {'User-agent': user_agent}
    try:
        redis = RedisOperater()
        proxy = redis.getRandomUsable()
        if proxy:
            proxies = {"http": "http://{proxy}".format(proxy=proxy), "https": "https://{proxy}".format(proxy=proxy)}
            response = requests.get(url, proxies=proxies, headers=headers, timeout=timeout)
        else:
            response = requests.get(url, headers=headers, timeout=timeout)
        code = response.status_code
        if (num_retries > 0):
            if (500 <= code < 600):
                return download(url, timeout, user_agent, num_retries-1)
        else:
            return None
        html = response.text
        return html
    except requests.ReadTimeout as ex:
        print('Download Timeout: {ex}'.format(ex=ex))
        return download(url, timeout, user_agent, num_retries - 1)
    except Exception as ex:
        print('Download error: {ex}'.format(ex=ex))

def download2(url, timeout=10, user_agent='wswp', num_retries=2):
    print('Downloading: {url}'.format(url=url))
    headers = {'User-agent': user_agent}
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        code = response.status_code
        if (num_retries > 0):
            if (500 <= code < 600):
                return download(url, timeout, user_agent, num_retries-1)
        else:
            return None
        html = response.text
        return html
    except requests.ReadTimeout as ex:
        print('Download Timeout: {ex}'.format(ex=ex))
        return download(url, timeout, user_agent, num_retries - 1)
    except Exception as ex:
        print('Download error: {ex}'.format(ex=ex))

def _base_test(ip):
    print('Test when proxy = {} is {}'.format(ip, validUsefulProxy(ip)))

if __name__ == '__main__':
    ip = '171.12.164.140:808'
    _base_test(ip)