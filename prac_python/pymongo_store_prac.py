from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 코딩 시작

# MongoDB에 inset 하기

# 'users'라는 collection에 {'name' : 'bobby', 'age' : 21}를 넣습니다.
db.users.insert_one({'name' : 'bobby', 'age' : 21})
db.users.insert_one({'name' : 'kay', 'age' : 27})
db.users.insert_one({'name' : 'john', 'age' : 30})