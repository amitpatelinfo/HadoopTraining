#!/usr/bin/python

# Format of the input data
# ip_address,identity , username, time, resource, status_code, size
# We want to return the output as (<minute-in-week slot>, <1>)
# We need to write them out to standard output, separated by a tab

import sys
from datetime import datetime

DATE_FORMAT = "%d/%b/%Y:%H:%M:%S"
MINUTE_OF_DAY = 60 * 24

for line in sys.stdin:
    data = line.split(" ")
    if len(data) == 10:
        time = data[3][1:]
        dt = datetime.strptime(time, DATE_FORMAT)
        week = dt.weekday()
        hour = dt.hour
        minute = dt.minute
        print "{0}\t1".format(((hour * 60) + minute) + (week * MINUTE_OF_DAY))
