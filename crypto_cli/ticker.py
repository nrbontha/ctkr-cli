#!/usr/bin/env python3

import ccxt

class Ticker(object):
    def __init__(self, exchange, base, quote='USD'):
        self.base = base.upper()
        self.quote = quote.upper()
        self.exchange = getattr(ccxt, exchange) 
        self.ticker = self.exchange().fetch_ticker('{}/{}' \
                                     .format(base.upper(), 
                                             quote.upper())) 

    @property
    def price(self):
        return self.ticker['last']

    @property
    def volume(self):
        return self.ticker['baseVolume']

