import os
import subprocess
from tkinter import filedialog
from tkinter import Tk
from datetime import datetime

def select_folder():
    Tk().withdraw()
    foldername = filedialog.askdirectory()  # show an "Open" dialog box and return the path to the selected folder
    return foldername

def concatenate_videos(input_folder, output_folder):
    # List all files in the input directory and filter for mp4 files
    video_files = [f for f in os.listdir(input_folder) if f.endswith('.mp4')]
    video_files.sort()  # make sure they are in alphabetical order
    
    # Create a list file for FFmpeg
    list_file = os.path.join(input_folder, 'videos.txt')
    with open(list_file, 'w') as f:
        for video_file in video_files:
            f.write(f"file '{os.path.join(input_folder, video_file)}'\n")
    
    # Generate a unique filename using the current date and time
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    output_file = os.path.join(output_folder, f'output_{timestamp}.mp4')

    # Build and run the FFmpeg command
    cmd = f'ffmpeg -f concat -safe 0 -i "{list_file}" -c copy "{output_file}"'
    subprocess.run(cmd, shell=True)

def main():
    # Determine the path of the script's directory
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Create the output folder as a subfolder of the script's directory
    output_folder = os.path.join(script_dir, 'outputs')
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    # Select the input folder and concatenate videos
    input_folder = select_folder()
    concatenate_videos(input_folder, output_folder)

if __name__ == '__main__':
    main()
