import datetime
import time
from . import config
import json

def str_to_unix_ts(s, fmt="%Y-%m-%d %H:%M:%S"):
    dt = datetime.datetime.strptime(s, fmt)
    t_tuple = dt.timetuple()
    return int(time.mktime(t_tuple))

def dt_to_str(dt):
	s = dt.strftime("%Y-%m-%d")
	return s

def data_file_writer(trades):
### writes JSON trade data to file
### WARNING: overwrites file if it already exists
    now = datetime.datetime.now()
    filename = "data/poloniex-" + dt_to_str(now) + ".json"
    f = open(filename, 'w+')
    json.dump(trades, f)
    f.close()
    print('Data written to ' + filename)

def data_file_reader(trades):
### reads JSON trade data from file
