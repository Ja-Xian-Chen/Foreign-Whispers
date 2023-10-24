from pytube import YouTube
file = open('links.txt','r')
links = file.readlines()

downloads = "videos"

for url in links:
    yt = YouTube(url)
    stream = yt.streams.get_by_itag(22)
    stream.download(downloads)
    print("Downloaded:", yt.title)
