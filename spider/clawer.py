# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Filename:   clawer.py
    Author:     Helyao
    Description:
        Claw html content from url
-------------------------------------------------
    Change Logs:
    2017-05-27 2:38pm   create
-------------------------------------------------
"""
import requests

def download(url, timeout=10, user_agent='wswp', num_retries=2):
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
