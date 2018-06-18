# Cryptocurrency Ticker CLI

`ctkr-cli` is a command line tool for analyzing cryptocurrency data with `ccxt` (and other open-source libraries).  

# Roadmap

v1.0:
- [x] get ticker data for any coin/exchange: price, volume, etc
- [ ] get exchange info: available exchanges, coins, symbols, etc.
- [ ] analysis: arbitrage, historical data, visualizations, etc.

Future:
- [ ] async request support
- [ ] execute trades on any US-based exchange (or non-US depending on exchange regulations)
- [ ] buy/sell decision algorithm
     - arbitrage/chaining: BTC -> BTC or BTC -> ETH -> MNR -> BTC across different exchanges
     - moving averages: rules for buying and selling based on long-term trends
- [ ] automated trading bot
