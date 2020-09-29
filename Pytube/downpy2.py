from pytube import YouTube
from pytube import Playlist
import re
import os

def ldownload_():
    pl = Playlist("https://www.youtube.com/playlist?list=PLXziV1DL41ojhfghjtP_jrU03iYy0vJZe")
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

        dir_ = "D:/VShare"
        urlstream[urlcount].download(dir_)

        file_path = 'D:/ShareDir'
        file_names = os.listdir(file_path)
        print(file_names)

        name="YouTube.mp4"
        if name in file_names:
            src = os.path.join(file_path, name)
            dst = str(count) +'.mp4'
            dst = os.path.join(file_path, dst)
            os.rename(src, dst)


        url2 = urlsum = urlstream = ""


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
    return urls

if __name__ == '__main__':
# ldownload_은 유튜브 리스트를 입력해 다운로드하고
#    ldownload_()

# fdownload는 input파일에 유튜브 주소를 입력해 다운로드한다.
    str_ = file_()
    fdownload_(str_)

    print("end")

