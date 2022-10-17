# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 14:20:50 2021

@author: Yago
"""

from headers import Headers
from exceptions import IdEmpty
from bs4 import BeautifulSoup as bs

class Info(Headers):
    __html= ""
    __countries_id = "countriesUL"
    __countries = {}
    __stocks = {}
    __sector = {}
    
    def __init__(self):
        Headers.__init__(self, path = "/stock-screener/")
        self.__html = bs(self.do_get.text, 'html.parser')
        self.get_countries()
    
    def get_countries(self):
        table = self.__html.find(id = self.__countries_id).find_all('li')
        self.__countries = {country.text[2:-1]: int(country['data-value']) for country in table} # I think that this is not necessary, @review
        
        
    def get_sector(self):
        # check the html to decide if it is posible to get all the info in one time
        pass
    
    def get_stocks_names(self, country_id):
        if not country_id: raise IdEmpty
        # I think that it is necessary to pass a country ID. Instead of doing it all in one time
        pass
    
    def get_all_stock_names(self):
        # This function shouldn't be used 
        pass
    
    @property
    def info_countries(self):
        return self.__countries
    
    @property
    def info_sector(self):
        return self.__sector 
    
    def __iter__(self):
        pass
    
    def __str__(self):
        return "Clase Info" # @todo a beatiful table