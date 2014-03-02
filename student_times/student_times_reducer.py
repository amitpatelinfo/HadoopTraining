#!/usr/bin/python

# Format of the input data
# (authorid , hour)
# We want to return the output as (authorid , hour)
# Our students come from all around the world, so we need to know both at what times of day the activity is the highest, and to know which of the students are active at that time.
#
#In this exercise your task is to find for each student what is the hour during which the student has posted the most posts. Output from reducers should be:
#If there is a tie: there are multiple hours during which a student has posted a maximum number of posts, please print the student-hour pairs on separate lines.

import sys
import operator

oldAuthorId = None

authorHourMap = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    #If something wrong then ignore the line
    if len(data_mapped) < 2:
        continue

    authorId, hour = data_mapped

    if oldAuthorId and oldAuthorId != authorId:
        result = sorted(authorHourMap.iteritems(), key=operator.itemgetter(1),reverse=True)
        resHour = -1
        for res in result:
            if resHour == -1:
                resHour = res[1]
            if resHour == res[1]:
                print oldAuthorId , "\t" , res[0] , "\t" , res[1]
        authorHourMap = {}

    oldAuthorId = authorId

    if hour in authorHourMap:
        authorHourMap[hour] += 1
    else:
        authorHourMap[hour] = 1
result = sorted(authorHourMap.iteritems(), key=operator.itemgetter(1),  reverse=True)
resHour = -1
for res in result:
    if resHour == -1 or resHour == res[1]:
        print oldAuthorId , "\t" , res[0]
