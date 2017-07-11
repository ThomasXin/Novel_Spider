# -*- coding:utf-8 -*-

from  spiders.db import ip_list

for ip in ip_list.find():
    print(ip['ipaddr'])