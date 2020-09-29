#pip install pytube
from pytube import YouTube

# sudo apt autoremove python
# apt-get install software-properties-common
# sudo add-apt-repository ppa:deadsnakes/ppa
# sudo apt-get install python3.5-dev
# apt-get install python-pip
# apt-get install python3-pip
#
# sudo update-alternatives --config python
# sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
# sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2
# sudo update-alternatives --config python
#
# python -m pip install --upgrade pip
#
#
# pip install pytube3 --upgrade


# url_=""
# while url_ != "x":
#     if url_ == "x":
#         break
#
#     url_ =input("주소를 입력(종료:x): ")
url = YouTube('https://www.youtube.com/watch?v=04V6_shtnpE')
url2 = url.streams.filter(progressive=True)
print(url.title)

for i in range(len(url2)):
    print(i, '.', url2[i])

vnum = int(input("다운로드 받을 화질은?"))

#url.streams.first().download()
dir_ = "D:/VShare/"
url2[vnum].download(dir_)


# from pytube import Playlist
# pl = Playlist("https://www.youtube.com/watch?v=BrGSW5UoHnI&list=PLNfg4W25Tapxp_2NyxHh-LF2AKKEkTzpq")
# pl.download_all()
