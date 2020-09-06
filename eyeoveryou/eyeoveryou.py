#!/usr/bin/env python

from decouple import config
import ipinfo
import pprint

access_token = config('IPINFOKEY')
handler = ipinfo.getHandler(access_token)
ip_address = '99.68.149.72'
details = handler.getDetails(ip_address)
pprint.pprint(details.all)