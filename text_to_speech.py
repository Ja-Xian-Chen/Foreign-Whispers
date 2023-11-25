import os
import pandas as pd
import torch
import torchaudio
from TTS.api import TTS

def process_csv_files(input_folder, output_folder):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC").to(device)    
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".csv"):
            csv_path = os.path.join(input_folder, file_name)
            df = pd.read_csv(csv_path)

            # Create subfolder for each CSV file
            subfolder_name = os.path.splitext(file_name)[0]
            subfolder_path = os.path.join(output_folder, subfolder_name)
            os.makedirs(subfolder_path, exist_ok=True)

            print(f"Processing CSV file: {file_name}")



input_folder = "data/target/translated"
output_folder = "data/target/speech"
process_csv_files(input_folder, output_folder)
