from moviepy.video.io.VideoFileClip import VideoFileClip

def cut_video(input_path, output_path, cut_seconds):
    # Create a VideoFileClip object from the input video
    clip = VideoFileClip(input_path)

    # Extract the first 5 seconds of the video
    subclip = clip.subclip(0, cut_seconds)

    # Write the extracted video to a new file
    subclip.write_videofile(output_path, fps=clip.fps)

    # Close the video clip objects
    clip.close()
    subclip.close()




