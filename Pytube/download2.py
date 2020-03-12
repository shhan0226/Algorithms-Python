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






