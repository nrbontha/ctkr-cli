# Cryptocurrency Ticker CLI

`ctkr-cli` is a command line tool for analyzing cryptocurrency data with `ccxt` (and other open-source libraries).  

# Roadmap

v1.0:
- [x] get ticker data for any coin/exchange: price, volume, etc
- [x] get exchange info: available exchanges, coins, symbols, etc.
- [x] async request support

Future:
- [ ] analysis: arbitrage, historical data, visualizations, etc.
- [ ] execute trades on any US-based exchange (or non-US depending on exchange regulations)
- [ ] buy/sell decision algorithm
     - arbitrage: BTC -> BTC across exchanges
     - chaining: BTC -> ETH -> MNR -> BTC across exchanges
     - moving averages: rules for buying and selling based on long-term trends
- [ ] automated trading bot


# Usage

Here are a few examples using the BTC/USD currency pair:

1. Get BTC/USD last prices on all exchanges

```
>>> ctkr exchange -s BTC/USD 
    {'_1btcxe': 'ExchangeError',
     'anxpro': 6012.91733,
     'bitbay': 6045.01,
     'bitflyer': 6035.6,
     'bitlish': 6133.0,
     'bitmex': 'ExchangeNotAvailable',
     'bitsane': 6404.28,
     'bitstamp': 6042.0,
     'bitstamp1': 6042.0,
     'bittrex': 6017.535,
     'btcturk': 6178.0,
     'btcx': 'ExchangeError',
     'cex': 6085.1,
     'cobinhood': 'ExchangeError',
     'coinbase': 6039.08,
     'coinfloor': 6631.0,
     'coingi': 'ExchangeNotAvailable',
     'coinmarketcap': 6072.09819029,
     'dsx': 6020.38001,
     'exmo': 6120.5996,
     'gatecoin': 6166.0,
     'gdax': 6038.99,
     'gemini': 6035.09,
     'getbtc': 6103.18,
     'independentreserve': 6135.89,
     'itbit': 6041.44,
     'kraken': 6034.5,
     'lakebtc': 6682.8,
     'livecoin': 6233.49221,
     'lykke': 6041.948,
     'mixcoins': 'ExchangeNotAvailable',
     'okcoinusd': 6286.89,
     'okex': 6001.11,
     'quadrigacx': 6439.96,
     'quoinex': 6046.81,
     'southxchange': 6165.7891,
     'tidebit': 6450.0,
     'wex': 8334.156,
     'yobit': 6384.34028297}

```

2. Get BTC/USD last prices for US-based exchanges

```
>>> ctkr exchange -s BTC/USD -c US
    {'bittrex': 6108.675,
     'btcx': 'ExchangeError',
     'coinbase': 6082.35,
     'coingi': 'ExchangeNotAvailable',
     'coinmarketcap': 6107.24570311,
     'gdax': 6082.35,
     'gemini': 6085.64,
     'itbit': 6083.55,
     'kraken': 6082.4,
     'lakebtc': 6721.65,
     'livecoin': 6279.39958,
     'okcoinusd': 6216.21,
     'okex': 6048.73}

```

3. Get BTC/USD "ask" prices for US-based exchanges

```
>>> ctkr exchange -s BTC/USD -c US -i ask_price
    {'bittrex': 6125.05,
     'btcx': 'ExchangeError',
     'coinbase': 6146.0,
     'coingi': 'ExchangeNotAvailable',
     'coinmarketcap': 'N/A',
     'gdax': 6090.74,
     'gemini': 6100.0,
     'itbit': 6090.09,
     'kraken': 6095.0,
     'lakebtc': 6727.05,
     'livecoin': 6281.50385,
     'okcoinusd': 6257.61,
     'okex': 6068.55}

```

4. Get BTC/USD last price on GDAX exchange

```
>>> ctkr gdax -s BTC/USD
    6097.26
```



To get the latest market data (updated pairs, symbols, and countries), use the following command: 

```
>>> ctkr exchange -i refresh
```
