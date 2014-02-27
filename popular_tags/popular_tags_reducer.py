#!/usr/bin/python

import sys
import operator

oldTagName = None
totalQuestions = 0
tagNameMap = {}

# Loop around the data
# It will be in the format (tagname)
# Output should be in format of (tagname, number_of_post) - number_of_post is a count of questions post in which we fount that tagname.

for tagName in sys.stdin:
    if tagName in tagNameMap:
        tagNameMap[tagName] += 1
    else:
        tagNameMap[tagName] = 1

result = sorted(tagNameMap.iteritems(), key=operator.itemgetter(1),reverse=True)
for key in range(0, 10):
    print "{0}\t{1}".format(result[key][0].strip(),result[key][1])
