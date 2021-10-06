# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 14:20:50 2021

@author: Yago
"""

from headers import Headers
from exceptions import IDEmpty
from bs4 import BeautifulSoup as bs

class Info(Headers):
    __html= ""
    __countriesID = "countriesUL"
    __countries = {}
    __stocks = {}
    __sector = {}
    
    def __init__(self):
        Headers.__init__(self, path = "/stock-screener/")
        self.__html = bs(self.doGet.text, 'html.parser')
        self.getCountries()
    
    def getCountries(self):
        table = self.__html.find(id = self.__countriesID).find_all('li')
        self.__countries = {country.text[2:-1]: int(country['data-value']) for country in table} # I think that this it is not necessarry, @review
        
        
    def getSector(self):
        # We have to review the html for decide if it is do posible all in one time
        pass
    
    def getStocksNames(self, countryID):
        if not countryID: raise IDEmpty
        # I think that it is necesarry pass a country ID. No do all in one time
        pass
    
    def getAllStockNames(self):
        # This function shouldn't use 
        pass
    
    @property
    def InfoCountries(self):
        return self.__countries
    
    @property
    def InfoSector(self):
        return self.__sector 
    
    def __str__(self):
        return "Clase Info" # @todo a beatiful table