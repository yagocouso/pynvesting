# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 20:30:27 2022

@author: Yago
"""

from core import get_info, Stock
from decorators import check_param
from exceptions import TypeNotValid

class Pyvesting():
    '''
    Class to extract the desired information about a specific asset.
    
    The information availabe to retrieve are:
    
    - stock information about the asset
    - news information about the asset
    - articles about the asset
    
    '''
    
    @staticmethod
    @check_param
    def get_stock(search):
        return get_info(search, stock = True)
    
    @staticmethod
    @check_param
    def get_news(search):
        return get_info(search, news = True)
    
    @staticmethod
    @check_param
    def get_articles(search):
        return get_info(search, articles = True)
    
    @staticmethod
    @check_param
    def get_all_stock_info(search):
        return get_info(search, stock = True, news = True, articles = True)
    
    @staticmethod
    def get_multi_stock_price(*stocks):
        string = ""
        for stock in stocks:
            if type(stock).__name__ != 'Stock': raise TypeNotValid
            string = string + "," + repr(stock)
        return string[1:]