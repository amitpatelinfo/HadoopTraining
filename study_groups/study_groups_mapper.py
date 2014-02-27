#!/usr/bin/python

# Format of the input data
# id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string,                  last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked
#
# We want to return the output as (id , parentid , authorid) - parenid will be 0 incase of question

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for data in reader:
    if len(data) == 19:
        id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = data
        if id != 'id':
            if node_type == 'question':
	    	    print "{0} 0 {1}".format(id,author_id)
            else:
                print "{0} {1} {2}".format(abs_parent_id,id, author_id)
