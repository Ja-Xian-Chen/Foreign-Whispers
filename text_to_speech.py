import os
import pandas as pd
import torch
from TTS.api import TTS

def text_to_speech(input_folder, output_folder):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC").to(device)    
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".csv"):
            df = pd.read_csv(os.path.join(input_folder, file_name))

            for index, row in df.iterrows():
                wav_file_path = os.path.join(output_folder, f"{index}.wav")
                tts.tts_to_file(text = row["translated_text"], file_path = wav_file_path)

if __name__ == "__main__":
    input_folder = "data/target/translated"
    output_folder = "data/target/speech"
    text_to_speech(input_folder, output_folder)
