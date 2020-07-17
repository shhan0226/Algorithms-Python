from pytube import YouTube

# input 파일에 주소 입력해서 다운로드받으면 됨

def download_(urllsit):
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
    download_(str_)
    print("end")

