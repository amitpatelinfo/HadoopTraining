#!/usr/bin/python

import sys

oldQuestionId = None
authorId = None
questionAuthorId = None

studyGroup = []

# Loop around the data
# It will be in the format (id, [list_of_stundets]

for line in sys.stdin:
    data_mapped = line.strip().split(" ")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    questionId, parentId, currentAuthorId = data_mapped

    if oldQuestionId == None and parentId == "0":
       questionAuthorId = currentAuthorId
    if oldQuestionId and oldQuestionId != questionId:
        if questionAuthorId != None and len(studyGroup) > 0:
            print oldQuestionId, "\t", studyGroup
        questionAuthorId = None
        if parentId == "0":
            questionAuthorId = currentAuthorId
        studyGroup = []

    oldQuestionId = questionId
    authorId = currentAuthorId
    studyGroup.append(authorId)

#if oldQuestionId != None and questionAuthorId != None and len(studyGroup) > 0:
print oldQuestionId, "\t", studyGroup
