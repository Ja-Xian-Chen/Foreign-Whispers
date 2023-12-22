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
    # download video
    vidFilename = filename + ".mp4"
    stream = yt.streams.get_by_itag(18)
    stream.download(videosPath, vidFilename)
    
    # convert video to audio
    audioFilename = filename + ".mp3"
    mp4_to_mp3(videosPath + vidFilename, audioPath + audioFilename)
    
    # download audio
    '''
    vidFilename = filename + ".webm"
    stream = yt.streams.get_by_itag(251)
    stream.download(audioPath, vidFilename)
    '''
    
    # download captions
    ccFilename = filename + ".txt"
    captions = yt.captions['a.en']
    with open(f"{captionsPath}{ccFilename}", 'w+') as wFile:
        wFile.write(captions.xml_captions)
    
    print("Downloaded:", vidFilename)

file.close()
