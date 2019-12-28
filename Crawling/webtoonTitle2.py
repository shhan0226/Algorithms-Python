from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://comic.naver.com/webtoon/weekday.nhn')
soup = bs(html.text,'html.parser')
html.close()

#요일별  웹툰 가져오기
#                  태그    속성     속성값
data1_list = soup.findAll('div', {'class':'col_inner'})
pprint(len(data1_list))


week_title_list = []

for data1 in data1_list:
    data2 = data1.findAll('a', {'class':'title'})
    title_list = [t.text for t in data2]

    #리스트에 추가
    week_title_list.append(title_list)
    #리스트에 더하기
    #week_title_list.extend(title_list)



pprint(week_title_list[6])
