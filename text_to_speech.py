import os
import pandas as pd
import torch
from TTS.api import TTS


def text_to_speech(input_folder, output_folder):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    # Initialize TTS model
    tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC").to(device)
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".csv"):
            csv_name = os.path.splitext(file_name)[0]
            csv_output_folder = os.path.join(output_folder, csv_name)
            
            # Create output folder 
            os.makedirs(csv_output_folder, exist_ok=True)
            df = pd.read_csv(os.path.join(input_folder, file_name))
            
            # Remove dashes
            df["translated_text"] = df["translated_text"].apply(lambda x: str(x).replace("-", " ") if pd.notna(x) else x)
            
            for index, row in df.iterrows():
                # Check if the column is not empty
                if pd.notna(row["translated_text"]) and row["translated_text"].strip() != "":
                    # WAV file path
                    wav_file_path = os.path.join(csv_output_folder, f"{index}.wav")
                    # Convert text to speech and save to the WAV file
                    tts.tts_to_file(text=row["translated_text"], file_path=wav_file_path)

input_folder = "data/target/translated"
output_folder = "data/target/speech"
text_to_speech(input_folder, output_folder)
