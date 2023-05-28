import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip

def crop_video(input_path, output_path, width, height):
    # Load the video clip
    video = VideoFileClip(input_path)

    # Calculate the desired aspect ratio
    aspect_ratio = width / height

    # Calculate the width and height of the cropped region
    video_aspect_ratio = video.size[0] / video.size[1]
    if video_aspect_ratio > aspect_ratio:
        new_width = int(video.size[1] * aspect_ratio)
        new_height = video.size[1]
    else:
        new_width = video.size[0]
        new_height = int(video.size[0] / aspect_ratio)

    # Calculate the coordinates of the region to crop
    x = (video.size[0] - new_width) // 2
    y = (video.size[1] - new_height) // 2

    # Crop the video
    cropped = video.crop(x1=x, y1=y, x2=x + new_width, y2=y + new_height)

    # Resize the cropped video to the desired resolution
    resized = cropped.resize((width, height))

    # Save the cropped and resized video
    output_file = os.path.join(output_path, os.path.basename(input_path))
    resized.write_videofile(output_file)

    # Close the video clip
    video.close()

# Input and output directories
input_directory = r'Y:\\New folder\\input'
output_directory = r'Y:\\New folder\\output'

# Desired resolution
width = 1080
height = 1920

# Process each .mp4 file in the input directory
for file_name in os.listdir(input_directory):
    if file_name.lower().endswith('.mp4'):
        input_path = os.path.join(input_directory, file_name)
        crop_video(input_path, output_directory, width, height)
