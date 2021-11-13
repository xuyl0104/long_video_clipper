## Music video clipper

Cut a long music video (usually contains several songs) into song clips (one song per clip).

### How to run the code?

- Preparation
  - Music video to be cut. Get the path of the video file;
  - Start time of each song and save the information into a file with the name of `timestamps.txt` ; (see the example file provided and save your info with the same format; the example file is the timestamps from [this video](https://www.youtube.com/watch?v=TL8EsYDpnwQ&t=3559s&ab_channel=SshinsMusicCorner))
  - Make sure ffmpeg has been installed on your machine; [How to install?](https://www.ffmpeg.org/) 
  - Python 3.x is a must;
  - Ready to go!

- Command to run

  - Modify `video_path` and `timestamps.txt` in` Section-1` of the code;
  - In command line, run `python ffmpeg.py`

  - Voila! Song clips are saved to the current folder, in both `.mp4` and `.m4a` formats.

