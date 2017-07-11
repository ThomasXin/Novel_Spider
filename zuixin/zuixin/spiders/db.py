import pymongo

client = pymongo.MongoClient('localhost', 27017)
quanshu = client['quanshu']
urls = quanshu['urls']
detailed = quanshu['detailed']
ip_list = quanshu['ip_list']