from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://comic.naver.com/webtoon/weekday.nhn')
soup = bs(html.text,'html.parser')
html.close()

#월요 웹툰 가져오기


data1 = soup.find('div', {'class':'col_inner'})
#                  태그    속성     속성값
#pprint(data1)

data2 = data1.findAll('a', {'class':'title'})
#pprint(data2)

#테스트만 추출
#title_list = []
#for t in data2:
#    title_list.append(t.text)

title_list = [t.text for t in data2]
#         리스트에 넣기<=for문을  
pprint(title_list)


