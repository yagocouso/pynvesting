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
    
    __request = None
    
    def __init__(self, authority = 'www.investing.com', mode = "navigate", path = '/', **headers_values):
        self.__url = self.checkhttp(authority) + path
        self.__headers['path'], self.__headers['authority'], self.__headers['sec-fetch-mode'] = path, authority, mode
        self.__headers.update(headers_values)
        self.assignMode
    
    @property
    def assignMode(self):
        self.__headers.update(self.__navigate if self.__headers['sec-fetch-mode'] == "navigate" else self.__cors)
        return self.__headers
    
    @property
    def data(self):
        return self.__request
        
    @staticmethod
    def checkhttp(url):
        return url if "http" in url else "https://" + url
    
    @property
    def doGet(self, **params):
        self.__request = requests.get(self.__url, headers=self.__headers, params = params)
        return self.__request
    
    @property
    def doPost(self, **payload):
        self.__request = requests.post(self.__url, headers=self.__headers, payload = payload)
        return self.__request
    
    def __call__(self):
        return self.__request
    
    def __str__(self):
        return str(self.__headers)
    
