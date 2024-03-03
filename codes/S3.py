from datetime import datetime as dt
import time as t


def time(start):
    print(dt.now().time())
    return dt.now().time().second - start


sec = 0
time_start = dt.now().time().second
while sec <= 5:
    t.sleep(1)
    sec = time(time_start)
