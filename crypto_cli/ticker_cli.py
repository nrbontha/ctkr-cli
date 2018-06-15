#!/usr/bin/env python3

import click
import json
from pprint import pprint
from ticker import Ticker

# $ctkr [exchange] [base] [quote] 


@click.command()
@click.argument('exch')
@click.argument('base')
@click.argument('quote')
@click.option(
    '-i', '--info', 
    default='ticker',
    help='Ticker information options.', 
    type=click.Choice(['ticker', 'price', 'volume'])
)
def get_ticker(exch, base, quote, info):
    """Get ccxt ticker info."""
    ticker = Ticker(exch, base, quote)
    output = None
    
    if info == 'price':
        output = '{} {}'.format(ticker.quote, ticker.price)
    elif info == 'volume':
        output = ticker.volume
    else:
        output = json.dumps(ticker.ticker, indent=2)

    click.echo(output)


if __name__ == '__main__':
    get_ticker()
