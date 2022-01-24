from email import header
from shutil import move
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

#  html 요청을 보내는 모듈인  request를 이용하여 response 객체를 받는다.
dataResponse = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo', headers=headers)

# html을 탐험하기 좋은 형태로 바꿔줌
soup = BeautifulSoup(dataResponse.text, 'html.parser')

teamInfos = soup.select('#regularTeamRecordList_table > tr')

for teamInfo in teamInfos:
    rank = teamInfo.select_one('th > strong').text
    team_name = teamInfo.select_one('td.tm > div > span').text
    team_win_rate = teamInfo.select_one('td:nth-child(7) > strong').text
    if (float(team_win_rate) > 0.5):
        print(rank, team_name, team_win_rate)


#regularTeamRecordList_table > tr:nth-child(1)
#regularTeamRecordList_table > tr:nth-child(1) > td:nth-child(7)