# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 13:35:27 2021

@author: Yago
"""

import requests

class Headers:
    __headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'accept': 'application/json, text/javascript, /; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'es-ES,es;q=0.9,gl;q=0.8',
        'sec-fetch-site': 'same-origin' 
    }
    
    __cors = {'sec-fetch-user':'?0', 'sec-fetch-dest':'empty', 
              'content-type': 'application/x-www-form-urlencoded',
              'x-requested-with': 'XMLHttpRequest'}
    
    __navigate = {'sec-fetch-user': '?1', 'sec-fetch-dest': 'document'}
    
    def __init__(self, authority = 'www.investing.com', mode = "navigate", path = '/', **headers_values):
        self.__url = self.checkhttp(authority) + path
        self.__headers['path'], self.__headers['authority'], self.__headers['sec-fetch-mode'] = path, authority, mode
        self.__headers.update({key:headers_values[key] for key in headers_values})
    
    @property
    def assignMode(self, mode):
        self.__headers.update(self.__navigate if mode == "navigate" else self.__cors)

    @staticmethod
    def checkhttp(url):
        return url if "http" in url else "https://" + url
    
    def doGet(self, **params):
        return requests.get(self.__url, headers=self.__headers, params = params)
    
    def doPost(self, **payload):
        return requests.get(self.__url, headers=self.__headers, payload = payload)
    
    def __call__(self):
        return self.headers
    
    def __str__(self):
        return str(self.__headers)  