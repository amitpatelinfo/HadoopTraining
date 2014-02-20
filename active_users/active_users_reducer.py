#!/usr/bin/python

# Format of the input data
# (authorid , id)
# We want to return the output as (authorid , total) - total will be total of questions,answers or comments
# We need to return the top 10 active users in the forum.

import sys
import operator

oldAuthorId = None
total = 0
activeAuthorsMap = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    #If something wrong then ignore the line
    if len(data_mapped) < 2:
        continue

    authorId, hour = data_mapped

    if oldAuthorId and oldAuthorId != authorId:
        activeAuthorsMap[oldAuthorId] = total
        total = 0

    oldAuthorId = authorId
    total += 1

result = sorted(activeAuthorsMap.iteritems(), key=operator.itemgetter(1),reverse=True)
for key in range(0, 10):
    print result[key][0], "\t", result[key][1]
