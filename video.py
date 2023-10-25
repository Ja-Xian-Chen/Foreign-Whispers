from pytube import YouTube

file = open('links.txt','r')
links = file.readlines()

videos = "videos"
captions = "captions"

for url in links:
    yt = YouTube(url)
    title = yt.title
    stream = yt.streams.get_by_itag(18)
    stream.download(videos)

    caption = yt.captions.get_by_language_code('en')
    filename = title.replace("\"", "").replace(":", "").replace(" ", "")+".txt"
    writeFile = open(f"{captions}\\{filename}", "w+")
    writeFile.write(caption.xml_captions)
    writeFile.close()
    
    print("Downloaded:", title)