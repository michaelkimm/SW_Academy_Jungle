from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# MongoDB에서 데이터 모두 보기
all_users = list(db.users.find({}))
for user in all_users:
    print(user)

db.users.update_one({'name':'bobby'},{'$set':{'age':15}})
all_users = list(db.users.find({}))
for user in all_users:
    print(user)
