#!/usr/bin/python
### checkin_by_city_mpr.py produces recrods with leading business_id
import sys
import json

for line in sys.stdin:
    try:
        r = json.loads(line.strip())
        print r['business_id']+"\t"+line.strip() 
    except:
        None  ### we don't produce an output row