# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 13:37:17 2021

@author: Yago
"""

from __version__ import __title__, __description__, __url__, __version__, __author__
from pyvesting import Pyvesting

apple = Pyvesting.get_stock("AAPL")
#lis = [Pyvesting.get_stock("AAPL"), Pyvesting.get_stock("AMD")]
#s = Pyvesting.get_multi_stock_price(lis[0], lis[1])
