#!/usr/bin/env python2.7
# twitter ETL : extracting JSON
import sys
import json

# input comes from STDIN (standard input)
for line in sys.stdin:
    jj = json.loads(line)
    u = jj["user"]["id_str"]
    for h in jj["entities"]["hashtags"]:
        #print '%s\t%s' % (u, h["text"])
        print '%s,%s\t%s' % (u, h["text"], 1)
