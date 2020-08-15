"""
Файл состоит из строк вида: `<host>\t<ip>\t<page>\n`, где host — корневой домен, ip — IP-адрес, page — «хвост» ссылки.

### Задача

Необходимо вывести 5 IP-адресов, которые встречаются в файле чаще других.
"""

import re

try:
    with open('hits.txt') as file_obj:
        data = file_obj.readlines()
except Exception as ex:
    print(ex)

ip_addresses = []
for record in data:
    search_ip = re.search(r'(\d\d\d|\d|\d\d).(\d\d\d|\d|\d\d).(\d\d\d|\d|\d\d).(\d\d\d|\d|\d\d)', record)
    if search_ip:
        ip = search_ip.group(0)
        ip_addresses.append(ip)
    else:
        print('Could not read IP-addresses')

ip_dict = {}

for ip_adr in ip_addresses:
    value = ip_dict.get(ip_adr)
    if value is None:
        ip_dict[ip_adr] = 1
    else:
        ip_dict[ip_adr] = value + 1

print(sorted(ip_dict, key=(lambda key: ip_dict[key]), reverse=True)[:5])

