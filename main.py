from chatgpt_module import generate_script
from tts_module import text_to_speech
from image_module import fetch_image
from video_module import create_video
from youtube_upload_module import upload_video

def run():
    print("Generating script...")
    script = generate_script()
    print("Converting to speech...")
    audio_path = text_to_speech(script)
    print("Fetching image...")
    image_path = fetch_image(script)
    print("Creating video...")
    video_path = create_video(image_path, audio_path, script)
    print("Uploading to YouTube...")
    upload_video(video_path)
    print("Done.")

if __name__ == "__main__":
    run()
