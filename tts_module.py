from gtts import gTTS
import os

def text_to_speech(sentences, filename="output/voice.mp3"):
    os.makedirs("output", exist_ok=True)
    text = ". ".join(sentences)
    tts = gTTS(text=text, lang="en")
    tts.save(filename)
    return filename
