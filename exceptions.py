# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 13:46:02 2021

@author: Yago
"""

class GeneralError(Exception):
    """General Error"""
    
class IdEmpty(Exception):
    """IDEmpty: The ID is not valid, please, use a valid ID"""
    
class CountryIdNotFound(Exception):
    """The country ID param it is not found, check this parameter"""