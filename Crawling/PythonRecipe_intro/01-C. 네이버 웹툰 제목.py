from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

#웹페이지 열고 소스 읽어 파싱하는 작업
html = requests.get('https://comic.naver.com/webtoon/weekday.nhn')
soup = bs(html.text,'html.parser')
html.close()

#-- [월요웹툰영역find] - [해당영역 제목 findAll] - [for로 text 추출] --#

#-- 월요 웹툰 가져오기 --#
data1 = soup.find('div', {'class':'col_inner'})
#                  태그    속성     속성값
#pprint(data1)

#제목 포함 영역 추출하기
data2 = data1.findAll('a', {'class':'title'})
#pprint(data2)


#for를 이용한 텍스트 추출 ; 테스트만 추출
#title_list = []
#for t in data2:
#    title_list.append(t.text)
#pprint(titile_list)

title_list = [t.text for t in data2]
#         리스트에 넣기<=for문을  
#pprint(title_list)

#----------------------------------#



#-- 요일별 웹툰영역 추출하기 --#

#요일별 영역 가져오기
data1_list=soup.findAll('div',{'class':'col_inner'})
# pprint(data1_list)

for data1 in data1_list:
    #제목 포함영역 추출하기
    data2=data1.findAll('a',{'class':'title'})
    # pprint(data2)

    #텍스트만 추출 2
    title_list = [t.text for t in data2]
#    pprint(title_list)


#-- 하나의 리스트로 묶기 --#
#전체 웹툰 리스트
week_title_list = []

for data1 in data1_list:
    #제목 포함영역 추출하기
    data2=data1.findAll('a',{'class':'title'})
    # pprint(data2)

    #텍스트만 추출 2
    title_list = [t.text for t in data2]
    # pprint(title_list)
    week_title_list.extend(title_list) #단순하게 값을 추가해 1차원으로 만들려면 extend
    # week_title_list.append(title_list) #요일별로 나눠 2차원 리스트를 만들려면 append

#pprint(week_title_list)



#-- 단순히 --#
#모든 웹툰 제목 영역 추출
data1=soup.findAll('a',{'class':'title'})
week_title_list = [ t.text for t in data1]
pprint(week_title_list)
