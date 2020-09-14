from decouple import config
import ipinfo
import pprint


def get_ip_info(ip):
    access_token = config('IPINFOKEY')
    handler = ipinfo.getHandler(access_token)
    return handler.getDetails(ip)


if __name__ == '__main__':
    info = get_ip_info('172.217.6.78')
    pprint.pprint(info.all)