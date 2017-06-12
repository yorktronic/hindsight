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

    def total_trade_count(trades):
    ### How many total trades have you made?
        num_trades = 0
        for currency_pair in trades:
            num_trades += len(trades[currency_pair])
        return num_trades

    return trades, total_trade_count(trades)

    def get_total_transaction_fees(trades):
        return None

# Average trade profitability
# Most profitable pair

# Get chart data