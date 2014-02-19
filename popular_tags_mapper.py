#!/usr/bin/python

# Format of the input data
# id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string,                  last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked
#
# We want to return the output as (tagname)
# Only need to get tagname if the node_type is question as per the requirment.

import sys
import re

def stripQuotes(data):
	return re.sub(r'^"|"$', '', data)

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 19:
        node_type = stripQuotes(data[5]).strip()
        tagnames = stripQuotes(data[2]).strip()
	    #Filter by nodetype as questions
        if node_type == "question":
            tags = tagnames.split(" ")
            for tag in tags:
                print "{0}".format(tag)
