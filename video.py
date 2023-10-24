from pathlib import Path
from pytube import YouTube

file = open('links.txt','r')
links = file.readlines()

videos = "videos"
captions = "caption"

for url in links:
    yt = YouTube(url)
    stream = yt.streams.get_by_itag(18)
    stream.download(videos)
    print("Downloaded:",yt.title)