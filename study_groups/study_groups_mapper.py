#!/usr/bin/python

# Format of the input data
# id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string,                  last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked
#
# We want to return the output as (id , parentid , authorid) - parenid will be 0 incase of question

import sys
import re

def stripQuotes(data):
	return re.sub(r'^"|"$', '', data)

for line in sys.stdin:
    data = line.split("\t")
    if len(data) == 19:
        id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = data
        if id != '"id"':
            nt = stripQuotes(node_type)
            if nt == 'question':
	    	    print "{0} 0 {1}".format(stripQuotes(id),stripQuotes(author_id))
            else:
                print "{0} {1} {2}".format(stripQuotes(abs_parent_id),stripQuotes(id), stripQuotes(author_id))
