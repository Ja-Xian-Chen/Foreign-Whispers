from pytube import YouTube

file = open('links.txt','r')
links = file.readlines()

videosPath = "data/videos/"
captionsPath = "data/captions/"

for url in links:
    yt = YouTube(url)
    vidFilename = yt.title.replace(' ', '_')
    stream = yt.streams.get_by_itag(18)
    stream.download(videosPath, vidFilename)

    ccFilename = vidFilename + ".txt"
    captions = yt.captions['a.en']
    with open(f"{captionsPath}{ccFilename}", 'w+') as wFile:
        wFile.write(captions.xml_captions)
    
    print("Downloaded:", vidFilename)

file.close()