# installed dependincies
# pip install -U openai-whisper

import whisper
import os
import csv

audioPath = "data/source/audio/"
transcriptsPath = "data/target/transcripts/"
dir = os.fsencode(audioPath)

# initialize whisper model
model = whisper.load_model("base")

# use to whisper to generate transcripts for each video
for fileEntry in os.listdir(dir):
    audioFilename = os.fsdecode(fileEntry)
    audioFilePath = os.path.join(audioPath, audioFilename)
    # make sure file exists
    if os.path.isfile(audioFilePath):
        print("-" * 25)
        print(f"Whisper is transcribing: {audioFilename}")
        result = model.transcribe(audioFilePath,fp16=False)
        # creates csv file
        csv_filename = f"{os.path.splitext(audioFilename)[0]}.csv"
        csv_path = os.path.join(transcriptsPath, csv_filename)
        
        with open(csv_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Start Time", "End Time", "Text"])

            for segment in result["segments"]:
                start_time = segment["start"]
                end_time = segment["end"]
                text = segment["text"]

                # Write the data to the CSV file
                csv_writer.writerow([start_time, end_time, text])
        print("transcript saved.")