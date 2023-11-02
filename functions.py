# dependencies
# pip install moviepy

from moviepy.editor import *

def mp4_to_mp3(mp4, mp3):
    audioFile = AudioFileClip(mp4)
    audioFile.write_audiofile(mp3)
    audioFile.close()

