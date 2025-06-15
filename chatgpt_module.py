import openai
import os

def generate_script():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = "Write a 4-sentence fun fact script for a viral educational animation video for YouTube Shorts. Make it punchy, interesting, and visually descriptive."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    script_text = response.choices[0].message['content']
    # Scripti cümle cümle böl
    sentences = [s.strip() for s in script_text.split('.') if s.strip()]
    return sentences
