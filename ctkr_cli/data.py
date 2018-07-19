#!/usr/bin/env python3

import async
import pickle
import ccxt
from exchange import (
    Exchange, 
    Marketplace, 
    Ticker
)


class MarketData(object):
    def __init__(self, file_path='data/market_data.p', refresh=False):
        if refresh:
            self.market_data = self._refresh_data(file_path)
        else:
            try:
                self.market_data = self._load_data(file_path)
            except FileNotFoundError:
                self.market_data = self._refresh_data(file_path)

    def _get_market(self, exch):
        try:
            mkt = Marketplace(exch)
            result = [exch, 
                     {
                      'countries': mkt.countries,
                      'coins': mkt.coins,
                      'symbols': mkt.symbols
                     }]
        except Exception as e:
            result = [exch, 
                     {
                      'countries': 'N/A',
                      'coins': 'N/A',
                      'symbols': 'N/A',
                      'error': type(e)
                     }]

        return result

    def _request_markets(self, n_workers=40):

        return async.run_loop(
            self._get_market, 
            n_workers, 
            ccxt.exchanges
        )

    def _save_data(self, file_path):

        with open(file_path, 'wb') as fp:
            pickle.dump(
                self.market_data, 
                fp, 
                protocol=pickle.HIGHEST_PROTOCOL
            )
   
    def _load_data(self, file_path):
        
        with open(file_path, 'rb') as fp:
            self.market_data = pickle.load(fp)
        return self.market_data

    def _refresh_data(self, file_path):

        self.market_data = self._request_markets()
        self._save_data(file_path)


class TickerData(MarketData):
    def __init__(self):
        MarketData.__init__(self) #self.market_data

    def __call__(self, symbol, data='last_price', n_workers=40):
        return self._request_tickers(symbol, data, n_workers)

    def _get_ticker(self, exchange, symbol, data):

        result = None
        try:
            ticker = Ticker(exchange, symbol)
        except Exception as e:
            result = type(e)
        else:
            if getattr(ticker, data):
                result = getattr(ticker, data)
        
        return [exchange, result]

    def _request_tickers(self, symbol, data, n_workers):
        
        markets = self._filter_markets(symbol)
        return async.run_loop(
            self._get_ticker, 
            n_workers, 
            markets, 
            symbol,
            data 
        )

    def _filter_markets(self, symbol):

        markets = filter(
            lambda exch: self.market_data[exch] 
            if symbol in self.market_data[exch]['symbols']
            else None, 
            self.market_data
        )

        return list(markets)

