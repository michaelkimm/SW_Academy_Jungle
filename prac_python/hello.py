from email import header
from shutil import move
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#  html 요청을 보내는 모듈인  request를 이용하여 response 객체를 받는다.
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    ac_tag = movie.select_one('td.ac > img')
    a_tag = movie.select_one('td.title > div > a')
    point_atr = movie.select_one('td.point')
    if a_tag is not None:
        rank = ac_tag['alt']
        title = a_tag.get_text()
        point = point_atr.get_text()
        print(rank, title, point)
#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img