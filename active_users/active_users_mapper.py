#!/usr/bin/python

# Format of the input data
# id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string,                  last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked
#
# We want to return the output as (authorid , id)
# We need to write them out to standard output, separated by a tab

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for data in reader:
    if len(data) == 19:
	id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = data
	if id != 'id':
		print "{0}\t{1}".format(author_id, id)


