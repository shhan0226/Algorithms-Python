from pytube import YouTube
from pytube import Playlist
from time import sleep

def ldownload_():
    pl = Playlist('https://www.youtube.com/watch?v=m8kIsOgDpnk&list=PL127T2Zu76FtYKMJqhX4cE-kzGqR302_y')
    list = pl.video_urls
    url2 = ""
    for url2_ in list:
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

        dir_ = "D:/VShare"
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

    str_ = file_()

    fdownload_(str_)
#ldownload_()

    print("end")

