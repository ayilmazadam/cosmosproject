from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

def create_text_scene(text, width=1280, height=720, bgcolor=(30, 144, 255), duration=3):
    img = Image.new("RGB", (width, height), bgcolor)
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        font = ImageFont.load_default()
    w, h = draw.textsize(text, font=font)
    position = ((width-w)//2, (height-h)//2)
    draw.text(position, text, font=font, fill="white")
    np_img = np.array(img)
    clip = ImageClip(np_img).set_duration(duration)
    return clip.crossfadein(1)

def generate_animation_video(sentences):
    os.makedirs("output", exist_ok=True)
    scenes = []
    colors = [(30, 144, 255), (46, 204, 113), (241, 196, 15), (231, 76, 60)]
    for i, sentence in enumerate(sentences):
        color = colors[i % len(colors)]
        scenes.append(create_text_scene(sentence, bgcolor=color, duration=3))
    final = concatenate_videoclips(scenes, method="compose")
    out_path = "output/animated_video.mp4"
    final.write_videofile(out_path, fps=24, codec="libx264")
    return out_path
