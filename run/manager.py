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
from spider.xiciNTProxyCrawler import run as XiciNTCrawlerRun
from spider.xiciNNProxyCrawler import run as XiciNNCrawlerRun
from spider.kuaiInhaProxyCrawler import run as KuaiInhaCrawlerRun
from spider.kuaiIntrProxyCrawler import run as KuaiIntrCrawlerRun
from filter.usableProxyHandler import run as UsableFilterRun
from filter.cacheProxyHandler import run as CacheFilterRun

from spider.blobProxyStatic import run as BlobStaticRun
from spider.xiciProxyStatic import run as XiciStaticRun

# for out-website
from spiderUSA.usProxyCrawler import run as UsCrawlerRun
from filter.usUsableProxyHandler import run as UsUsableFilterRun
from filter.usCacheProxyHandler import run as UsCacheFilterRun

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

# AllFreeProxy Mode
def allFreeProxy():
    proList = list()
    pro1 = Process(target=ServerRun, name='ServerRun')
    proList.append(pro1)
    pro2 = Process(target=XiciNTCrawlerRun, name='XiciNTCrawlerRun')
    proList.append(pro2)
    pro3 = Process(target=XiciNNCrawlerRun, name='XiciNNCrawlerRun')
    proList.append(pro3)
    pro4 = Process(target=KuaiInhaCrawlerRun, name='KuaiInhaCrawlerRun')
    proList.append(pro4)
    pro5 = Process(target=KuaiIntrCrawlerRun, name='KuaiIntrCrawlerRun')
    proList.append(pro5)
    pro6 = Process(target=BlobStaticRun, name='BlobStaticRun')
    proList.append(pro6)
    pro7 = Process(target=XiciApiRun, name='XiciApiRun')
    proList.append(pro7)
    pro8 = Process(target=UsableFilterRun, name='UsableFilterRun')
    proList.append(pro8)
    pro9 = Process(target=CacheFilterRun, name='CacheFilterRun1')
    proList.append(pro9)
    pro10 = Process(target=CacheFilterRun, name='CacheFilterRun2')
    proList.append(pro10)
    pro11 = Process(target=CacheFilterRun, name='CacheFilterRun3')
    proList.append(pro11)
    for pro in proList:
        pro.start()
    for pro in proList:
        pro.join()

# AllFreeProxy Out-website Mode
def allUsFreeProxy():
    proList = list()
    pro1 = Process(target=ServerRun, name='ServerRun')
    proList.append(pro1)
    pro2 = Process(target=UsCrawlerRun, name='UsCrawlerRun')
    proList.append(pro2)
    pro3 = Process(target=UsUsableFilterRun, name='UsUsableFilterRun')
    proList.append(pro3)
    pro4 = Process(target=UsCacheFilterRun, name='UsCacheFilterRun')
    proList.append(pro4)
    for pro in proList:
        pro.start()
    for pro in proList:
        pro.join()

def allFreeProxyCache():
    proList = list()
    pro1 = Process(target=ServerRun, name='ServerRun')
    proList.append(pro1)
    pro2 = Process(target=XiciStaticRun, name='XiciStaticRun')
    proList.append(pro2)
    pro3 = Process(target=KuaiInhaCrawlerRun, name='KuaiInhaCrawlerRun')
    proList.append(pro3)
    pro4 = Process(target=KuaiIntrCrawlerRun, name='KuaiIntrCrawlerRun')
    proList.append(pro4)
    pro5 = Process(target=BlobApiRun, name='BlobApiRun')
    proList.append(pro5)
    pro6 = Process(target=UsableFilterRun, name='UsableFilterRun')
    proList.append(pro6)
    pro7 = Process(target=CacheFilterRun, name='CacheFilterRun1')
    proList.append(pro7)
    pro8 = Process(target=CacheFilterRun, name='CacheFilterRun2')
    proList.append(pro8)
    pro9 = Process(target=CacheFilterRun, name='CacheFilterRun3')
    proList.append(pro9)
    pro10 = Process(target=CacheFilterRun, name='CacheFilterRun4')
    proList.append(pro10)
    pro11 = Process(target=CacheFilterRun, name='CacheFilterRun5')
    proList.append(pro11)
    pro12 = Process(target=CacheFilterRun, name='CacheFilterRun6')
    proList.append(pro12)
    pro13 = Process(target=CacheFilterRun, name='CacheFilterRun7')
    proList.append(pro13)
    pro14 = Process(target=CacheFilterRun, name='CacheFilterRun8')
    proList.append(pro14)
    pro15 = Process(target=CacheFilterRun, name='CacheFilterRun9')
    proList.append(pro15)
    pro16 = Process(target=CacheFilterRun, name='CacheFilterRun10')
    proList.append(pro16)
    pro17 = Process(target=CacheFilterRun, name='CacheFilterRun11')
    proList.append(pro17)
    for pro in proList:
        pro.start()
    for pro in proList:
        pro.join()


if __name__ == '__main__':
    # onlyXiciFreeApi()
    # onlyKuaiFreeApi()
    # allFreeProxy()
    allFreeProxyCache()
    # allUsFreeProxy()