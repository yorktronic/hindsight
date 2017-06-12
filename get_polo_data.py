import poloniex
from lib import config
from lib import util

START = util.str_to_unix_ts(config.START)
polo = poloniex.Poloniex(config.POLONIEX['key'], config.POLONIEX['secret'])
balance = polo.returnBalances()

def get_nonzero_balance(balance):
### returns only balances with nonzero values
    balance_nonzero = {}
    for b in balance:
        b_int = float(balance[b])
        if b_int > 0:
            balance_nonzero[b] = b_int

    return balance_nonzero

def get_trade_history(start):
### Get entire polo trade history
    trades = polo.returnTradeHistory(start=START)
    return trades

def save_trade_history(trades):
### Save trade history to file
    util.data_file_writer(trades)

def total_trade_count(trades):
### How many total trades have you made?
    num_trades = 0
    for currency_pair in trades:
        num_trades += len(trades[currency_pair])
    
    return num_trades

def all_trade_pairs(trades):
    return trades.keys()

def total_transaction_fees(trades):
    return None

def sort_trades(trades):
### Sorts trades by whether ETH, BTC, XMR, or USDT was used
    sorted_trades = {}
    all_pairs = all_trade_pairs(trades)
    
    for pair in all_pairs:
        root_coin = pair.split("_")[0]
        sorted_trades[root_coin][pair] = trades[pair]

    return sorted_trades

# Average trade profitability
# Most profitable pair

# Get chart data