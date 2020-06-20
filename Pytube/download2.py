from pytube import YouTube

flag = "go"

while flag != "no":
    urltag = "https://www.youtube.com/watch?v="
    s = input("url :")
    print(urltag+s)

    url = YouTube(urltag+s)
    url2 = url.streams.filter(progressive=True)
    print("Title : " + url.title)

    for i in range(len(url2)):
        print(i, '.', url2[i])

    vnum = int(input("다운로드 받을 화질은?"))
    dir_ = "D:/VShare"
    url2[vnum].download(dir_)

    flag = input("go? no? :")



"""
# https://www.youtube.com/watch?v=auKdde7Anr8&list=PLlMkM4tgfjnJhhd4wn5aj8fVTYJwIpWkS
# https://www.youtube.com/playlist?list=PLlMkM4tgfjnJhhd4wn5aj8fVTYJwIpWkS
from pytube import Playlist

pl = Playlist('https://www.youtube.com/watch?v=auKdde7Anr8&list=PLlMkM4tgfjnJhhd4wn5aj8fVTYJwIpWkS')

list = pl.video_urls
print("A")
print(list)

print(list)
#pl.playlist_id()
#pl.download_all()

"""





