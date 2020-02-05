#윈도우에서의 설치 명령어  
#pip install requests   
#pip install BeautifulSoup4  

from pprint import pprint

import requests
from bs4 import BeautifulSoup as bs

#--1. 웹페이지 가져오기--#
html = requests.get('https://search.naver.com/search.naver?query=날씨')
#pprint(html.text)

#--2. 파싱 ; 파싱 작업으로 각 요소에 적근 가능하게 만 --#
soup = bs(html.text,'html.parser')
#pprint(soup)

#--3. 요소 1개 찾기 --#
data1 = soup.find('div', {'class':'detail_box'})
#                  태그    속성     속성값
#pprint(data1)

#--4. 요소 모두 찾기 ; 인덱스는 0부터 시작됨 --#
data2 = data1.findAll('dd')
#pprint(data2)
#pprint(data2[2])

#--5. 내부 텍스트 추출 --#
find_dust = data2[2].find('span',{'class':'num'})
pprint(find_dust)

#.txt는해당 부분의 텍스트만 출력
pprint(find_dust.text)

