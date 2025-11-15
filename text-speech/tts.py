import pyttsx3

engine = pyttsx3.init()            # driver: sapi5 on Windows, nsss on macOS, espeak on Linux
engine.setProperty("rate", 160)    # words per minute
engine.setProperty("volume", 0.9)  # 0.0 to 1.0

voices = engine.getProperty("voices")
for i, v in enumerate(voices):
    print(i, v.id, v.name)

engine.setProperty("voice", voices[1].id)

engine.say("Hello! This is pyttsx3 speaking.")
engine.runAndWait()

# from gtts import gTTS
# import os

# tts = gTTS("Hello! This is a test using gTTS.", lang='en')
# tts.save("speech.mp3")

# # Windows: open the MP3 with default player
# os.startfile("speech.mp3")

