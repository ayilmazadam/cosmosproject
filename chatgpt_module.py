import openai
import os

def generate_script(konu):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = f"Create a dramatic, viral and catchy short video script in English about: {konu}. Use an engaging narration, keep it under 90 seconds. Make sure it feels intense, like a true crime or big secret reveal."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # istersen 4o da yazabilirsin, gpt-4o için.
        messages=[{"role": "user", "content": prompt}]
    )
    script = response['choices'][0]['message']['content']
    return script
