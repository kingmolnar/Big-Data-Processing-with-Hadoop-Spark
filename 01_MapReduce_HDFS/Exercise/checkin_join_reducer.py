#!/usr/bin/python
### checkin_join_reducer.py

## This reducer joins two data sets (business.json and checkin.json) on their business_id
import sys
import json
import numpy as np

current_bid = None
bid = None
reco = None

business_list = []
checkin_list = []

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    bid, rjson = line.split('\t', 1)

    if current_bid == bid:
        if '"type": "checkin"' in rjson:
            checkin_list.append(rjson)
        else:
            business_list.append(rjson)
        
    else:
        if current_bid:
            for b in business_list:
                for c in checkin_list:
                    print '%s\t%s\t%s' % (current_bid, b.strip(), c.strip())
        current_bid = bid
        business_list = []
        checkin_list = []
        if '"type": "checkin"' in rjson:
            checkin_list.append(rjson)
        else:
            business_list.append(rjson)

# do not forget to output the last word if needed!
if current_bid == bid:
    for b in business_list:
        for c in checkin_list:
            print '%s\t%s\t%s' % (current_bid, b.strip(), c.strip())
            
