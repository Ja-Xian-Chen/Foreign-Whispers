from pytube import YouTube
from functions import *

file = open('links.txt','r')
links = file.readlines()

videosPath = "data/source/videos/"
audioPath = "data/source/audio/"
captionsPath = "data/source/captions/"

for url in links:
    yt = YouTube(url)
    filename = yt.title.replace(' ', '_')

    vidFilename = filename + ".mp4"
    stream = yt.streams.get_by_itag(18)
    stream.download(videosPath, vidFilename)

    audioFilename = filename + ".mp3"
    mp4_to_mp3(videosPath + vidFilename, audioPath + audioFilename)

    ccFilename = filename + ".txt"
    captions = yt.captions['a.en']
    with open(f"{captionsPath}{ccFilename}", 'w+') as wFile:
        wFile.write(captions.xml_captions)
    
    print("Downloaded:", vidFilename)

file.close()