from gtts import gTTS
import os

file = open("file.txt", "r").read()

speech = gTTS(text=file, lang='en', slow=False)
speech.save("speech.mp3")
os.system("speech.mp3")