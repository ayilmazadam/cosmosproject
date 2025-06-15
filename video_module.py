from moviepy.editor import VideoFileClip, AudioFileClip

def add_audio_to_video(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)
    final = video.set_audio(audio)
    out_path = "output/final_video.mp4"
    final.write_videofile(out_path, fps=24, codec="libx264")
    return out_path
