from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle 

# 코딩 시작
movie = db.movies.find_one({'title':'매트릭스'})
matrixStar = movie['star']

print(matrixStar)
# db.movies.update_one({'title':'매트릭스'}, {'$set':{'star':0}})

# movie = db.movies.find_one({'title':'매트릭스'})
# movieStar = movie['star']
# print(movieStar)