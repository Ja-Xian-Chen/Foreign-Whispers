import os
import pandas as pd
import torch
from TTS.api import TTS

def text_to_speech(input_folder, speech_folder, target_language="de"):
    # Load TTS model
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".csv"):
            input_path = os.path.join(input_folder, file_name)
            
            df = pd.read_csv(input_path)

            # Perform TTS for each translated text
            for index, row in df.iterrows():
                translated_text = row["translated_text"]
                output_audio_path = os.path.join(speech_folder, f"{file_name}_{index}.wav")
                tts.tts_to_file(text=translated_text, language=target_language, filename=output_audio_path)

input_folder = "data/target/translated"
speech_folder = "data/target/speech"
target_language = "de"

text_to_speech(input_folder, speech_folder, target_language)
