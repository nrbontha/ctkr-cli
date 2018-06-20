#!/usr/bin/env python3

import ccxt
import click
import json
from pprint import pprint

# TODO: CLI COMMANDS
# get ticker price
# $ctkr [exchange] -b [base] -q [quote] -i [info]
# $ctkr gdax -b btc -q usd

# list exchanges
# $ctkr -a

# get all exchange info
# $ctkr gdax -a

#TODO: pickledb 
#TODO: async ticker requests 

def get_exchanges():
    pprint(ccxt.exchanges) 

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

class Market(Exchange):
    def __init__(self, exch_name):
        Exchange.__init__(self, exch_name)
        self.markets = self.get_markets()

    @property
    def coins(self):
        return list({m['base'] for m in self.markets if m['active']}) 

    @property
    def symbols(self):
        return [m['symbol'] for m in self.markets if m['active']]

class Ticker(Exchange):
    def __init__(self, exch_name, symbol):
        Exchange.__init__(self, exch_name)
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
    def volume(self):
        return self.ticker['baseVolume']


@click.command()
@click.argument('exchange')
@click.argument('base')
@click.argument('quote')
@click.option(
    '-i', '--info', 
    default='ticker',
    help='Ticker information options.', 
    type=click.Choice(['ticker', 'price', 'volume'])
)
def main(exchange, base, quote, info):
    """Get ccxt ticker info."""
    ticker = Ticker(exchange, base, quote)
    output = None
    
    if info == 'price':
        output = '{} {}'.format(ticker.quote, ticker.price)
    elif info == 'volume':
        output = ticker.volume
    else:
        output = json.dumps(ticker.ticker, indent=2)

    click.echo(output)


if __name__ == '__main__':
    main()


