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
from filter.cacheProxyHandler import run as FilterRun

# OnlyXiciFreeApi Mode
def onlyXiciFreeApi():
    proList = list()
    pro1 = Process(target=XiciApiRun, name='XiciApiRun')
    proList.append(pro1)
    pro2 = Process(target=FilterRun, name='FilterRun')
    proList.append(pro2)
    pro3 = Process(target=ServerRun, name='ServerRun')
    proList.append(pro3)
    for pro in proList:
        pro.start()
    for pro in proList:
        pro.join()

if __name__ == '__main__':
    onlyXiciFreeApi()