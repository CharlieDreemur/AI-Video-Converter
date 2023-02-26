from moviepy.video.io.VideoFileClip import VideoFileClip

def cut_video(input_path, output_path, cut_seconds):
    clip = VideoFileClip(input_path).subclip(cut_seconds)
    clip.write_videofile(output_path, fps=clip.fps)




