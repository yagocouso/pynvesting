# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 20:07:38 2022

@author: Yago
"""

from exceptions import ParamIsEmpty

def check_param(func):
    '''
    check if there's no imput for the functions'
    '''
    def decorator(search = None):
        if not search: raise ParamIsEmpty 
        return func(search)
    return decorator