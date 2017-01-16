#!/usr/bin/python
### checkin_by_city_reducer.py

import sys
import json
import numpy as np

current_city_state = None
city_state = None
reco = None

# the vector to aggregate checkins per hour per day
check_vec = np.zeros(7*24)
check_n = 0


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    city_state, rjson = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        reco = json.loads(rjson)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_city_state == city_state:
        for k in reco['checkin_info'].keys():
            k2 = k.split('-')
            h = int(k2[0])
            d = int(k2[1])
            c = int(reco['checkin_info'][k])
            check_vec[h*7+d] += c
        check_n += 1
    else:
        if current_city_state and (check_n > 0):
            print '%s|%s' % (current_city_state, '|'.join([str(x) for x in check_vec/check_n]))
        current_city_state = city_state
        check_vec = np.zeros(7*24)
        for k in reco['checkin_info'].keys():
            k2 = k.split('-')
            h = int(k2[0])
            d = int(k2[1])
            c = int(reco['checkin_info'][k])
            check_vec[h*7+d] += c
        check_n = 1


# do not forget to output the last word if needed!
if current_city_state and (check_n > 0):
            print '%s|%s' % (current_city_state, '|'.join([str(x) for x in check_vec/check_n]))
