# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Filename:   manager.py
    Author:     Helyao
    Description:
        Lanuch project by selected mode
-------------------------------------------------
    Change Logs:
    2017-06-02 2:43pm   create
-------------------------------------------------
"""
import sys
from multiprocessing import Process

sys.path.append('../')
from api.server import run as ServerRun
from spider.xiciProxyApi import run as XiciApiRun
from spider.blobProxyApi import run as BlobApiRun
from spider.kuaiProxyCrawler import run as KuaiCrawlerRun
from filter.usableProxyHandler import run as UsableFilterRun
from filter.cacheProxyHandler import run as CacheFilterRun

# If the cache is bigger and bigger, should lanuch more CacheFilterRun process
# If the usable proxies rate is low, should lanuch more UsableFilterRun process

# OnlyXiciFreeApi Mode
def onlyXiciFreeApi():
    proList = list()
    pro1 = Process(target=XiciApiRun, name='XiciApiRun')
    proList.append(pro1)
    pro2 = Process(target=UsableFilterRun, name='UsableFilterRun')
    proList.append(pro2)
    pro3 = Process(target=ServerRun, name='ServerRun')
    proList.append(pro3)
    for pro in proList:
        pro.start()
    for pro in proList:
        pro.join()

# OnlyKuaiFreeCrawler Mode
def onlyKuaiFreeApi():
    proList = list()
    pro1 = Process(target=XiciApiRun, name='XiciApiRun')
    proList.append(pro1)
    pro2 = Process(target=KuaiCrawlerRun, name='KuaiCrawlerRun')
    proList.append(pro2)
    pro3 = Process(target=UsableFilterRun, name='UsableFilterRun')
    proList.append(pro3)
    pro4 = Process(target=CacheFilterRun, name='CacheFilterRun')
    proList.append(pro4)
    pro5 = Process(target=ServerRun, name='ServerRun')
    proList.append(pro5)
    for pro in proList:
        pro.start()
    for pro in proList:
        pro.join()

# AllFreeProxy Mode
def allFreeProxy():
    proList = list()
    pro1 = Process(target=KuaiCrawlerRun, name='KuaiCrawlerRun')
    proList.append(pro1)
    pro2 = Process(target=UsableFilterRun, name='UsableFilterRun')
    proList.append(pro2)
    pro3 = Process(target=CacheFilterRun, name='CacheFilterRun')
    proList.append(pro3)
    pro4 = Process(target=ServerRun, name='ServerRun')
    proList.append(pro4)
    for pro in proList:
        pro.start()
    for pro in proList:
        pro.join()


if __name__ == '__main__':
    # onlyXiciFreeApi()
    # onlyKuaiFreeApi()
    allFreeProxy()