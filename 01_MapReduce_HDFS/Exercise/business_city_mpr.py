#!/usr/bin/python

import sys
import json

for line in sys.stdin.readlines():
    try:
        r = json.loads(line.strip())
        print r['city']+"/"+r['state'] 
    except:
        None  ### we don't produce an output row