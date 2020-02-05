from bs4 import BeautifulSoup
from pprint import pprint
import requests, re, os
from urllib.request import urlretrieve

#-- 저장 폴더 생성 --#
#os모듈을 참조하고 아래 함수들을 사용
#os.path.isdir : 이미 디렉토리가 있는지 검사
#os.path.join : 현재 경로를 계산하여 입력으로 들어온 텍스트를 합하여 새로운 경로를 만듬
#os.makedirs : 입력으로 들어온 경로로 폴더를 생성

try:
    if not (os.path.isdir('image')):
        os.makedirs(os.path.join('image'))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 생성 실패!")
        exit()

#웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

#요일별 웹툰영역 추출하기
data1_list=soup.findAll('div',{'class':'col_inner'})
# pprint(data1_list)

#전체 웹툰 리스트
li_list = []
for data1 in data1_list:
    #제목+썸내일 영역 추출
    li_list.extend(data1.findAll('li')) #해당 부분을 찾아 li_list와 병합

#pprint(li_list)
    
#-- 각각 썸네일과 제목 추출하기 --#
#img 태그를 추출한 뒤 속성값을 추출
#img 태그에 썸네일 이미지의 주소와 웹툰 제목이 속성값으로 존재
#추출한 데이터에 ['속성명'] 명시
    
for li in li_list:
    img = li.find('img')
    title = img['title']
    img_src = img['src']
#    print(title,img_src)

#-- 특수문자 처리 --#
#변경은 replace를 하면 되는데, 여기서는 정규식 표현을 이용한 re모듈을 사용
    title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title)

#-- 이미지 다운로드 --#
#from urllib.request import urlretrieve 를 추가한 뒤,
#urlretrieve 호출 시에 링크와 저장할 파열명을 넣으면 됨

    urlretrieve( img_src , './image/'+title+'.jpg')
                   #주소,   파일경로+파일명+확장자


    



    
