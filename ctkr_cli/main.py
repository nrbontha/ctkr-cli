#!/usr/bin/env python3

import click
import json
from models import (
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
    '-c', '--country', 
    help='Country options.'
)
@click.option(
    '-i', '--info', 
    help='Information options.'
)
def main(exchange, symbol, country, info):
    """Get ccxt ticker info."""
    result = None

    print(country)

    if not info:
        info = 'last_price'

    if exchange == 'exchange':
        if symbol:
            tkr = TickerData()
            result = tkr(symbol, country, info)
        else:
            if info:    
                if info == 'all':
                    result = ccxt.exchanges
                elif info == 'refresh':
                    return MarketData(refresh=True)
                else: 
                    result = 'error: unknown info flag `%s`' % (str(info))
            else:
                result = 'error: no info or symbol flag supplied'

    else:
        if symbol:
            tkr = Ticker(exchange, symbol)
            result = getattr(tkr, info) if info else tkr.ticker
        else:
            mkt = Marketplace(exchange)
            if info:
                result = getattr(mkt, info)
            else:
                result = mkt.markets

    pprint(result)


if __name__ == '__main__':
    main()




