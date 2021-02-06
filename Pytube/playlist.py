from pytube import Playlist
import re
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' +  directory)

pl = Playlist("https://www.youtube.com/playlist?list=PLVsNizTWUw7FJot9rAiWBJN3V9EZFBFZX")
print("[ Title:", pl.title, "]")

title_name = pl.title
dir_ = "D:/ShareDir"
createFolder(dir_ +"/"+ title_name )

flag = 1
for video in pl.videos:
    if flag == 1:
        print(video.streams)
        itag_name = input("itag input: ")
        flag =0
    video.streams.get_by_itag(itag_name).download(dir_ +"/"+ title_name)
    print("download! >>> ", video.streams.get_by_itag(itag_name).title)


