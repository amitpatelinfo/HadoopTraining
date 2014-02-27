#!/usr/bin/python

import sys

oldQuestionId = None

resultPath = None

questionLength = -1
totalAns = 0
answerAvgLength = 0
answerTotalLength = 0

postLength = 0

# Loop around the data
# It will be in the format (id , parentid , length_of_post)
# parentid will be 0 incase of question
#
# We need to return the (questionid , length_of_post_question , avg_length_of_all_answer)
# We need to ignore the answer which do not have any parents

for line in sys.stdin:
    data_mapped = line.split(" ")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    questionId, parentId, originalPostLength = data_mapped

    if oldQuestionId == None and parentId == "0":
        questionLength = int(originalPostLength)

    if oldQuestionId and oldQuestionId != questionId:
        if totalAns != 0:
            answerAvgLength = float(answerTotalLength / totalAns)
        if questionLength != -1:
                print "{0}\t{1}\t{2}".format(oldQuestionId, questionLength, answerAvgLength)
        questionLength = -1
        if parentId == "0":
            questionLength = int(originalPostLength)
        totalAns = 0
        answerTotalLength = 0
        answerAvgLength = 0

    oldQuestionId = questionId
    if parentId != "0":
        totalAns += 1
        answerTotalLength += float(originalPostLength)

if oldQuestionId != None:
    if totalAns != 0:
        answerAvgLength = float(answerTotalLength / totalAns)
    if questionLength != -1:
        print "{0}\t{1}\t{2}".format(oldQuestionId, questionLength, answerAvgLength)
