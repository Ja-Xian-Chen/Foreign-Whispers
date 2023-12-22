# Foreign Whispers
In this project you will develop a solution that will accept as input youtube videos from the 60 minutes channel and output the video but with spoken and written subtitles to another language of your choosing.

## Milestone 1
Source Videos and Closed Captions 
Write a python API that will download the video and its closed captions from youtube.
Access 10 videos from the 60 minutes channel and more specifically from the Interviews playlist and download them to your local environment.

## Milestone 2
Write a Python API that will separate the audio from the video and convert it to text. For this you will use libraries such as openai/whisper

## Milestone 3:Source Text to Target Text 
Write a Python API that will translate the text from English to a language of your choosing. Please note you need to select the language from the list of languages that can be served by the TTS Milestone. You can use any library you want for this task except commercial ones that include Google Translate, Microsoft Translate, OpenAI etc.

## Milestone 4: Target Text to Speech
Write a Python API that will convert the translated text to speech. You can use any library you want for this task except commercial ones. For example, you can use TTS

##Milestone 5a: Stitching it all together 
Build a UI in Hugging Face Spaces and Streamlit Spaces that will accept as input a youtube video and will output the video with subtitles to a language of your choosing.
