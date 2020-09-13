#!/usr/bin/env python

import pprint
from ip_info_client import get_ip_info
from metaweather import get_weather

details = get_ip_info('151.101.65.69')
weather = get_weather(details.all['loc'])
pprint.pprint(details.all)
pprint.pprint(weather)
