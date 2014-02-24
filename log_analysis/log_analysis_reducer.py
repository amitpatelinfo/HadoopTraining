#!/usr/bin/python

import sys

totalCount = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the <minute-in-week slot> and value as a count 1.
#
# We need to count the total for single <minute-in-week slot> and return result as (<minute-in-week slot>, <total>)

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisValue = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", totalCount
        oldKey = thisKey;
        totalCount = 0

    oldKey = thisKey
    totalCount += int(thisValue)

if oldKey != None:
    print oldKey, "\t", totalCount

