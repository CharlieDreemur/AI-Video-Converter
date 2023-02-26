from moviepy.editor import VideoFileClip
import ffmpeg
from moviepy.editor import VideoFileClip, AudioFileClip
def extract_audio(input_path, audio_path):
    video_clip = VideoFileClip(input_path)

    # Extract the audio from the video clip
    audio_clip = video_clip.audio

    # Save the audio to a file
    audio_clip.write_audiofile(audio_path)

    # Release the resources used by the video and audio clips
    video_clip.close()
    audio_clip.close()

def add_audio_to_video(video_path, audio_path, combined_path):
    # Load the video clip
    video_clip = VideoFileClip(video_path)

    # Load the audio clip
    audio_clip = AudioFileClip(audio_path)

    # Set the audio of the video clip to the extracted audio
    video_clip = video_clip.set_audio(audio_clip)

    # Write the new video clip to the output file
    video_clip.write_videofile(combined_path)

'''if __name__=="__main__":
    input_path = 'test1.mp4'
    audio_path = 'my_audio.mp3'
    extract_audio(input_path, audio_path)
    video_path = 'video.mp4'
    combinedvideo_path = 'my_combined_video.mp4'
    add_audio_to_video(video_path, audio_path, combinedvideo_path)'''