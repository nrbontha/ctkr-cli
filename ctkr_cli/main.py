#!/usr/bin/env python3

import click
import json
from exchange import (
    Exchange, 
    Marketplace, 
    Ticker
)
from data import (
    MarketData,
    TickerData
)
from pprint import pprint


@click.command()
@click.argument('exchange')
@click.option(
    '-s', '--symbol', 
    help='Symbol options.'
)
@click.option(
    '-i', '--info', 
    help='Information options.'
)
def main(exchange, symbol, info):
    """Get ccxt ticker info."""
    result = None

    if exchange == 'exchange':
        if symbol:
            ticker = TickerData()
            result = ticker(symbol, info) if info else ticker(symbol)
        else:
            if info:    
                if info == 'all':
                    result = ccxt.exchanges
                else: 
                    result = 'error: unknown info flag `%s`' % (str(info))
            else:
                result = 'error: no info or symbol flag supplied'

    else:
        if symbol:
            data = Ticker(exchange, symbol)
            result = getattr(data, info) if info else data.ticker
        else:
            data = Marketplace(exchange)
            if info:
                result = getattr(data, info)
            else:
                result = data.markets

    pprint(result)


if __name__ == '__main__':
    main()




