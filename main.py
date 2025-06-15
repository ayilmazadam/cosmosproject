from chatgpt_module import generate_script
from tts_module import text_to_speech
from animation_module import generate_animation_video
from video_module import add_audio_to_video

def run():
    print("Generating script...")
    script = generate_script()
    print("Creating animation video...")
    video_path = generate_animation_video(script)
    print("Generating voiceover...")
    audio_path = text_to_speech(script)
    print("Combining video and audio...")
    add_audio_to_video(video_path, audio_path)
    print("Done! Output: output/final_video.mp4")

if __name__ == "__main__":
    run()
