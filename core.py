# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 11:32:20 2021

@author: Yago
"""

from info import Info
from headers import Headers
from exceptions import CountryIDNotFound
from time import sleep


#class Historic(Headers, Info):
#    pass




#class ActValue(Headers, Info):
#    pass



class Stock(Headers):
    
    _pair_id = 0
    _symbol = ''
    _name = ''
    #_country = 0
    _country_id = 0
    _sector_id = 0
    _industry_id = 0
    _exchange = 0
    _exchange_id = 0
    
    def __init__(self, pair_id, symbol, name, country_id, sector_id, industry_id, exchange, exchange_id):
        Headers.__init__(self, path = "/stock-screener/")
        self._pair_id = pair_id
        self._symbol = symbol
        #self._country = country
        self._country_id = country_id
        self._sector_id = sector_id
        self._industry_id = industry_id
        self._exchange = exchange
        self._exchange_id = exchange_id
        
    def __str__(self):
        return self._symbol
    
    def __repr__(self):
        return self._symbol
    
    def __add__(self, new_stock):
        if type(new_stock) == str: return f',{new_stock},{self._exchange}:{self._symbol}'
        return f'{self._exchange}:{self._symbol},{new_stock._exchange}:{new_stock._symbol}'


def AllStocks(country_id, industry_id = None, sector_id = None, exchange_id = None):
    pass
country_id = 5
if not country_id: raise CountryIDNotFound
page = 1
totalCount = 1
stocks_list = []
request = Headers(path = "/stock-screener/Service/SearchStocks", mode = "cors")
payload = {'country[]': str(country_id), 'order[col]':'name_trans', 'order[dir]':'a'}  
while len(stocks_list) < totalCount:
    print(f'Completado: {len(stocks_list) / totalCount * 100} %')
    payload['pn'] = str(page)
    data = request.doPost(payload=payload).json()
    if not len(stocks_list): totalCount = int(data['totalCount'])
    stocks_list.extend([Stock(
        stk['pair_ID'], 
        stk['stock_symbol'],
        stk['name_trans'],
        #country_id,
        country_id,
        stk['sector_id'] if 'sector_id' in stk.keys() else '',
        stk['industry_id'] if 'industry_id' in stk.keys() else '', 
        stk['exchange_trans'],
        stk['exchange_ID']
        ) for stk in data['hits']])
    page += 1
    sleep(1)
    #return stocks_list
   
    """payload = {
            'country[]': '5',
            #'sector': '7,5,21,12,3,16,8,17,13,9,19,1,6,18,15,20,14,23,2,4,10,11,22',
            #'industry': '81,56,110,59,119,41,120,68,67,88,124,125,51,72,147,136,47,12,144,8,50,111,2,151,71,9,105,69,45,117,156,46,13,94,102,95,58,100,101,87,31,106,6,38,112,150,79,107,30,77,131,130,149,160,113,165,28,158,5,103,163,170,60,18,26,137,135,44,35,53,166,48,141,49,142,143,55,129,126,139,169,114,153,78,7,86,10,164,132,1,34,154,3,127,146,115,11,121,162,62,16,108,24,20,54,33,83,29,152,76,133,167,37,90,85,82,104,22,14,17,109,19,43,140,89,145,96,57,84,118,93,171,27,74,97,4,73,36,42,98,65,70,40,99,39,92,122,75,66,63,21,159,25,155,64,134,157,128,61,148,32,138,91,116,123,52,23,15,80,168,161',
            #'equityType': "ORD,DRC,Preferred,Unit,ClosedEnd,REIT,ELKS,OpenEnd,Right,ParticipationShare,CapitalSecurity,PerpetualCapitalSecurity,GuaranteeCertificate,IGC,Warrant,SeniorNote,Debenture,ETF,ADR,ETC",
            #'exchange[]': '4',
            'pn': str(1),
            'order[col]':'name_trans', 
            'order[dir]':'a'
    }  """
    #♣a = requests.post("https://www.investing.com/stock-screener/Service/SearchStocks", headers=headers, data=payload)
    #a.status_code
    #datos = pd.DataFrame(a.json()['hits'])

listStock = AllStocks(5)

