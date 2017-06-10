import poloniex
from lib import config
from lib import util
import datetime
import time

START = util.str_to_unix_ts(config.START)

polo = poloniex.Poloniex(config.POLONIEX['key'], config.POLONIEX['secret'])
balance = polo.returnBalances()

# Get non-zero balances
balance_nonzero = {}

for b in balance:
    b_int = float(balance[b])
    if b_int > 0:
        balance_nonzero[b] = b_int

# Get entire trade history
trades = polo.returnTradeHistory(start=START)

# How many total trades have you made?
def total_trade_count(trades):
    num_trades = 0
    for currency_pair in trades:
        num_trades += len(trades[currency_pair])
    return num_trades