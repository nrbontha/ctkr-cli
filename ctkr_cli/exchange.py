#!/usr/bin/env python3

import ccxt

class Exchange(object):
    def __init__(self, exch_name):
        self.exchange = getattr(ccxt, exch_name)()

    @property
    def countries(self):
        return self.exchange.countries

    def get_markets(self):
        return self.exchange.fetch_markets()

    def get_ticker(self, symbol):
        return self.exchange.fetch_ticker(symbol)


class Marketplace(Exchange):
    def __init__(self, exch_name):
        Exchange.__init__(self, exch_name)
        self.markets = self.get_markets()

    @property
    def coins(self):
        return list({m['base'] for m in self.markets if m['active']}) 

    @property
    def symbols(self):
        return [m['symbol'] for m in self.markets if m['active']]


class Ticker(Marketplace):
    def __init__(self, exch_name, symbol):
        Marketplace.__init__(self, exch_name)
        self.ticker = self.get_ticker(symbol)

    @property
    def datetime(self):
        return self.ticker['datetime']

    @property
    def timestamp(self):
        return self.ticker['timestamp']

    @property
    def last_price(self):
        return self.ticker['last']

    @property
    def ask_price(self):
        return self.ticker['ask']

    @property
    def bid_price(self):
        return self.ticker['bid']

    @property
    def high_price(self):
        return self.ticker['high']

    @property
    def low_price(self):
        return self.ticker['low']

    @property
    def base_volume(self):
        return self.ticker['baseVolume']

    @property
    def quote_volume(self):
        return self.ticker['quoteVolume']

