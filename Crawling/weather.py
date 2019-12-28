from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
#pprint(html.text)

soup = bs(html.text,'html.parser')
#pprint(soup)

data1 = soup.find('div', {'class':'detail_box'})
#                  태그    속성     속성값
#pprint(data1)

data2 = data1.findAll('dd')
#pprint(data2)
#pprint(data2[2])

find_dust = data2[2].find('span',{'class':'num'})
pprint(find_dust)

#.txt는해당 부분의 텍스트만 출력
pprint(find_dust.text)

