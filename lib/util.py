import datetime
import time
from . import config

def str_to_unix_ts(s, fmt="%Y-%m-%d %H:%M:%S"):
    dt = datetime.datetime.strptime(s, fmt)
    t_tuple = dt.timetuple()
    return int(time.mktime(t_tuple))