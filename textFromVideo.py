import speech_recognition as sr
import moviepy.editor as mp
from datetime import datetime

location = input("Video location: ")

if ".mp4" not in location:
    location += ".mp4"

clip = mp.VideoFileClip(location)
clip.audio.write_audiofile("video.wav",codec='pcm_s16le')
print("Extracting text ...")

r = sr.Recognizer()
audio = sr.AudioFile("video.wav")

fileName = str(datetime.now())[-6:] + ".txt"

with audio as source:
    audio = r.record(source, duration=100)
    text = r.recognize_google(audio)
    with open(fileName, 'w') as f:
        f.write(text)
    print(f"Successfully saved text from the given video to {fileName}.")