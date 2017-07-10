# -*- coding:utf-8 -*-
import pymongo
import time
client = pymongo.MongoClient('localhost', 27017)
quanshu = client['quanshu']
detailed = quanshu['detailed']
urls = quanshu['urls']
s = 0
for sign in detailed.find().limit(1500):
    if sign['sign'] == '149':
        s += 1
        print(sign)
print(s)
# s = set([url['url'] for url in detailed.find()])
# # for detail in detailed.find({}, {'url': 1, '_id': 0}).limit(1000000):
#
# print(len(s))
# print('***********************************8')
# while True:
#     print(detailed.find().count())
#     time.sleep(5)

# for url in urls.find():
#     if url['url'].split('/')[-1]!='index.html':
#         print(url)