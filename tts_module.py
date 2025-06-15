from gtts import gTTS
import os

def text_to_speech(script, lang="en"):
    os.makedirs("voices", exist_ok=True)
    output_path = "voices/output.mp3"
    tts = gTTS(text=script, lang=lang)
    tts.save(output_path)
    return output_path
