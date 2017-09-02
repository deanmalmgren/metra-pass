#!/usr/bin/env python

"""stupid script to calculate whether I should buy a monthly vs 10-ride pass
"""

import sys
import math

n_one_way_trips = int(sys.argv[1])

# https://metrarail.com/maps-schedules/train-lines/UP-W/fares#quicktabs-fare_information
fares = {
    'monthly': 228.00,
    '10-ride': 72.00,
    'one-way': 8.00,
}

if n_one_way_trips * fares['one-way'] < fares['10-ride']:
    print "buy {} one-way trips".format(n_one_way_trips)
elif fares['10-ride'] / 10 * n_one_way_trips < fares['monthly']:
    print "buy {} ten-ride passes".format(float(n_one_way_trips) / 10)
else:
    print "buy monthly pass"
