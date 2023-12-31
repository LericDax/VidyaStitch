# VidyaStitch

VidyaStitch is a Python script that uses FFmpeg to automatically concatenate videos from a selected directory. The script ensures that the last frame of one video matches the first frame of the next. The output video is saved in an 'outputs' subfolder with a unique timestamp in its name.

## Prerequisites

- Python 3.6 or later
- FFmpeg: This script uses FFmpeg to concatenate videos. Please ensure that FFmpeg is installed and added to your system's PATH. If FFmpeg is not installed, you can download it from the [official FFmpeg website](https://ffmpeg.org/download.html).

## Usage

1. Run the script.
2. A dialog box will appear. Select the directory containing the videos you want to concatenate. Make sure all videos are in .mp4 format.
3. The script will automatically concatenate the videos (in alphabetical order of their filenames) and save the output in the 'outputs' subfolder, with a unique name like 'output_20230726123015.mp4', where '20230726123015' is the current date and time.

## License

This project is licensed under the terms of the MIT license.
