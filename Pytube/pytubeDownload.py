from pytube import YouTube
from pytube import Playlist
import re
import os

def ldownload_():
    pl = Playlist("https://www.youtube.com/playlist?list=PLXe1xUfF_4Dl_Pyr33z8rMkEgVuOb9wVt")
    pl._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    count = 0
    list = pl.video_urls
    for url2_ in list:
        count = count + 1

        print(url2_)
        urlsum = YouTube(url2_)
        urlstream = urlsum.streams.filter(progressive=True)

        print("Title : " + urlsum.title)
        if "YouTube" in urlsum.title:
            print("Check >>>>>>>>>>>>  :" + url2_)

        urlcount = -1
        for i in range(len(urlstream)):
            urlcount += 1
            print(i, '.', urlstream[i])
        print("index =", urlcount)

        dir_ = "D:/ShareDir"
        urlstream[urlcount].download(dir_)
        url2_ = ""




def fdownload_(urllsit):
    urltag = "https://www.youtube.com/watch?v="

    for url_ in urllsit :
        urlsum = ""
        print(urltag + url_)

        urlsum = YouTube(urltag + url_)
        urlstream = urlsum.streams.filter(progressive=True)

        print("Title : " + urlsum.title)

        urlcount = -1
        for i in range(len(urlstream)):
            urlcount += 1
            print(i, '.', urlstream[i])

        dir_ = "D:/ShareDir"
        urlstream[urlcount].download(dir_)

def file_():
    urls = []
    f = open("input", 'r')
    lines = f.readlines()
    for line in lines:
        strs = line.strip("\n").split('?v=')
        url_ = strs[1]
        urls.append(url_)
    f.close()
    print(urls)
    return urls

if __name__ == '__main__':
# ldownload_은 유튜브 리스트를 입력해 다운로드하고
#    ldownload_()

# fdownload는 input파일에 유튜브 주소를 입력해 다운로드한다.
    str_ = file_()
    fdownload_(str_)

    print("end")

