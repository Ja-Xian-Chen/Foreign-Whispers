import os
import pandas as pd
from transformers import T5Tokenizer, T5ForConditionalGeneration

def translate_text(text, target_language="es"):
    model_name = "t5-base"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    # Tokenize and generate translation
    input_text = f"translate English to {target_language}: {text}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    translation_ids = model.generate(input_ids)
    translated_text = tokenizer.decode(translation_ids[0], skip_special_tokens=True)

    return translated_text

def translate(input_folder, output_folder, target_language="es"):
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".csv"):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)
            
            df = pd.read_csv(input_path)
            # Translate each text
            df["translated_text"] = df["Text"].apply(lambda x: translate_text(x, target_language))
            # Save new CSV file
            df.to_csv(output_path, index=False)


input_folder = "data/target/transcripts"
output_folder = "data/target/translated"
target_language = "de"

translate(input_folder, output_folder, target_language)
