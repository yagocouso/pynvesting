# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 13:46:02 2021

@author: Yago
"""

class GeneralError(Exception):
    def __str__(self):
       return "General Error"
    
class IdEmpty(Exception):
    def __str__(self):
       return "IDEmpty: The ID is not valid, please, use a valid ID"
    
class CountryIdNotFound(Exception):
    def __str__(self):
       return "The country ID parameter is not found, check this parameter"
    
class ParamIsEmpty(Exception):
    def __str__(self):
       return  "The parameter is mandatory, please, enter a parameter"
   
class TypeNotValid(Exception):
    def __str__(self):
       return  "The type must be Stock"
   
class BadRequest(Exception):
    def __str__(self):
       return  "The resquest isn't correct"