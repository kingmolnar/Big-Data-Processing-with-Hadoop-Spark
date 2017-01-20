#!/usr/bin/env python

import sys
import json
# input comes from STDIN (standard input)
for line in sys.stdin:
    try:
        r = json.loads(line)
        ##for f in r['friends']:
        ## printing COMMA seperated lines from a list of values
        print ','.join([r['user_id'], r['name'], r['review_count'], r['average_stars']])

