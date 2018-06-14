#!/usr/bin/env python3

import click
import ccxt
from pprint import pprint

# $crypto [exchange] [base] [quote] 

def get_last_price(exchange, base, quote):
    
    exchange = getattr(ccxt, exchange)
    return exchange().fetch_ticker('{}/{}'.format(base, quote))['last']


if __name__ == "__main__":
    
    get_last_price(exchange='gdax', base='BTC', quote='USD')


