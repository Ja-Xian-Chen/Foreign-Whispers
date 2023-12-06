import os
import csv

def seconds_to_srt_time(seconds):
    minutes, seconds = divmod(float(seconds), 60)
    return f"{int(minutes):02d}:{int(seconds):02d}"

def convert_csv_to_srt(csv_folder, srt_folder):
    for csv_file in os.listdir(csv_folder):
        if csv_file.endswith(".csv"):
            csv_file_path = os.path.join(csv_folder, csv_file)
            srt_file_path = os.path.join(srt_folder, os.path.splitext(csv_file)[0] + ".srt")
            
            with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                
                with open(srt_file_path, 'w', encoding='utf-8') as srt_file:
                    subtitle_number = 1
                    for row in reader:
                        start_time = seconds_to_srt_time(row['Start Time'])
                        end_time = seconds_to_srt_time(row['End Time'])
                        text = row['translated_text']

                        srt_file.write(f"{subtitle_number}\n")
                        srt_file.write(f"{start_time} --> {end_time}\n")
                        srt_file.write(f"{text}\n\n")

                        subtitle_number += 1


csv_folder_path = "data/target/translated" 
srt_output_folder = "srts"

if not os.path.exists(srt_output_folder):
    os.makedirs(srt_output_folder)

convert_csv_to_srt(csv_folder_path, srt_output_folder)
