# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 13:35:27 2021

@author: Yago
"""

import requests
import random

USER_AGENT = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/74.0.3729.157 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/79.0.3945.88 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    'Mozilla/5.0 (X11; Datanyze; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.24 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20100101 Firefox/21.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
    ]


class Headers:
    """
    Defines all the functions and parameters needed to request the info to investing.com
    """
    __headers = {
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
        self.__url = self.check_http(authority) + path
        self.__headers['path'], self.__headers['authority'], self.__headers['sec-fetch-mode'] = path, authority, mode
        self.__headers.update(headers_values)
        self.assign_mode
    
    @property
    def assign_mode(self):
        self.__headers.update(self.__navigate if self.__headers['sec-fetch-mode'] == "navigate" else self.__cors)
        return self.__headers
    
    @property
    def data(self):
        return self.__request
        
    @staticmethod
    def check_http(url):
        return url if "http" in url else "https://" + url
    
    @staticmethod
    def user_agent():
        global USER_AGENT
        return random.choice(USER_AGENT) 
    
    def do_get(self, **params):
        params = self.cleanparams(params)
        self.__headers['user-agent'] = self.user_agent()
        self.__request = requests.get(self.__url, headers=self.__headers, params = params)
        return self.__request

    def do_post(self, **payload):
        self.__headers['user-agent'] = self.user_agent()
        self.__request = requests.post(self.__url, headers=self.__headers, data = payload)
        return self.__request
    
    def cleanparams(self, params):
        if params["since"]: 
            params["from"] = params["since"]
            del params["since"]
        return params
    
    def __call__(self):
        return self.__request
    
    def __str__(self):
        return str(self.__headers)
    
