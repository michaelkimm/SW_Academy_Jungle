from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.dbjungle

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

# @app.route('/memo', methods=['GET'])
# def listing():
#     # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
#     # 2. articles라는 키 값으로 영화정보 내려주기
#     return jsonify({'result':'success', 'msg':'GET 연결되었습니다!'})

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def post_article():
	# 1. 클라이언트로부터 데이터를 받기
    url_receive = request.form['url_give']      # 클라이언트로부터 url 받기
    comment_receive = request.form['comment_give']  # 클라이언트로부터 comment를 받기

	# 2. meta tag를 스크래핑하기
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')

    url_title = og_title['content']
    url_description = og_description['content']
    url_image = og_image['content']

    article = { 'url' : url_receive, 'title' : url_title, 'desc' : url_description, 'image' : url_image, 'comment' : comment_receive }

    # 3. mongoDB에 데이터 넣기
    db.articles.insert_one(article)
    
    return jsonify({'result': 'success', 'msg':'스크래핑 및 DB에 삽입 완료!'})

@app.route('/memo', methods=['GET'])
def read_articles():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기 (Read)
    result = list(db.articles.find({}, {'_id': 0}))
    # 2. articles라는 키 값으로 article 정보 보내주기
    return jsonify({'result': 'success', 'articles': result})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)