# installed dependincies
# pip install -U openai-whisper

import whisper
import json
import os

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
        result = model.transcribe(audioFilePath)
        
        transcript = {
            "text": result["text"],
            "segments": result["segments"]
        }

        transcriptFilename, _ = os.path.splitext(audioFilename)
        transcriptFilename = transcriptFilename + "_transcript.json"

        transcriptPath = transcriptsPath + transcriptFilename

        with open(transcriptPath, "w") as jsonFile:
            json.dump(transcript, jsonFile, ensure_ascii=False, indent=4)

        print("transcript saved.")
