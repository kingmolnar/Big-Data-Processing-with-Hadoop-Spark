#!/usr/bin/python
# get data in the format business_id {business.json} {checkin.json}
# produce records with city/state key

import sys
import json

for line in sys.stdin:
    line = line.strip()
    try:
        bid, bjson, cjson = line.split('\t')
        brec = json.loads(bjson)
        print "%s/%s\t%s" % (brec['city'].strip(), brec['state'].strip(), cjson)
    except:
        None
        
