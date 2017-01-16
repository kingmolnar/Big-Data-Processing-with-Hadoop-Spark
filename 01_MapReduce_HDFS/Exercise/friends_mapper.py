#!/usr/bin/env python

import sys
import json
# input comes from STDIN (standard input)
for line in sys.stdin:
    r = json.loads(line)
    for f in r['friends']:
        ## printing tab seperated lines from a list of values
        print '\t'.join([r['name'], r['user_id'], f])