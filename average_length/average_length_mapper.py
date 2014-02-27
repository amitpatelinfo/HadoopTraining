#!/usr/bin/python

# Format of the input data
# id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string,                last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked
#
# We want to return the output as (id , parentid , length_of_post) - parenid will be 0 incase of question
# We need to ignore the comments.

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_NONE)

for data in reader:
    if len(data) == 19:
	id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = data
    if node_type == 'question':
        print "{0} 0 {1}".format(id,len(body))
    if node_type == 'answer':
        print "{0} {1} {2}".format(abs_parent_id,id, len(body))
