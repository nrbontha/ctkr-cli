#!/usr/bin/env python3

import ccxt
import click
import json
from pprint import pprint


# TICKER PRICE
# ctkr [exchange] -b [base] -q [quote] -i [info]
# ctkr gdax -b btc -q usd

# LIST EXCHANGES
# ctkr -a

# EXCHANGE INFO
# ctkr gdax -a

# ctkr exchange -a
# ctkr price -b btc -q usd -i

class Ticker(object):
    def __init__(self, exchange, base, quote):
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


