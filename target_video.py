from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
import pandas as pd
from pathlib import Path
import os

def generate_target_video(video_path, transcript_path, audio_path, destination_dir):
    
    video = VideoFileClip(video_path)
    
    # Add subtitles
    generator = lambda txt: TextClip(txt, font='Arial', fontsize=24, color='white', align='center', stroke_width=1, size=(video.w - 40, None), method='caption')
    
    subs = pd.read_csv(transcript_path)
    subs_data = [((start, end), text) for start, end, text in zip(subs['Start Time'], subs['End Time'], subs['translated_text'])]
    
    subtitles = SubtitlesClip(subs_data, generator)
    target = CompositeVideoClip([video, subtitles.set_position(('center','bottom'))])
    
    # Add audio clips
    audio_clips = []
    for i, row in subs.iterrows():
        audio_clip = AudioFileClip(os.path.join(audio_path, str(i) + '.wav')).set_start(row['Start Time'])
        audio_clips.append(audio_clip)
    
    composite_audio = CompositeAudioClip(audio_clips)
    target = target.set_audio(composite_audio)

    video_name = os.path.basename(video_path)
    destination_path = os.path.join(destination_dir, video_name)
    target.write_videofile(destination_path, codec='libx264', fps=24)

#Ukraine’s_First_Lady_Olena_Zelenska:_The_60_Minutes_Interview
#Facebook_Whistleblower_Frances_Haugen:_The_60_Minutes_Interview
video_name = "Facebook_Whistleblower_Frances_Haugen:_The_60_Minutes_Interview"
    
video_path = f"data/source/videos/{video_name}.mp4"
transcript_path = f"data/target/translated/{video_name}.csv"
audio_path = f"data/target/speech/{video_name}/"
destination_dir = "data/target/target_videos/"

generate_target_video(video_path, transcript_path, audio_path, destination_dir)