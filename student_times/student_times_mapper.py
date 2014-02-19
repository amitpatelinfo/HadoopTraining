#!/usr/bin/python

# Format of the input data
# id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string,                  last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked
#
# We want to return the output as (authorid , hour)
# We need to write them out to standard output, separated by a tab

import sys
import re
from datetime import datetime

def stripQuote(data):
	return re.sub(r'^"|"$', '', data)

DATE_FORMAT = "%Y-%m-%d %H:%M:%S.%f"

for line in sys.stdin:
    data = line.split("\t")
    if len(data) == 19:
	id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = data
	if id != '"id"':
		date_added = stripQuote(added_at)
		date_added = date_added[:date_added.rfind('+'):]
		hour = datetime.strptime(date_added, DATE_FORMAT).hour
		print "{0}\t{1}".format(stripQuote(author_id), hour)


