#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os

# Section-1
# path of essential files
# Modify this before you cut your own files
video_path = "/Users/xuyunlong/Movies/Youtube-dl/henryng_cut.mp4"
timestamps_path = "./timestamps.txt"

start_time_list = []
song_title_list = []
count = 0

# Section-2
# get the start time of each song
# get the title of each song
with open(timestamps_path, 'r') as timestamps_file:
    for line in timestamps_file:
        start_time = line.split(' ')[0]
        song_title = line.split(' ')[1]

        start_time_list.append(start_time)
        song_title_list.append(song_title.strip())
        count = count + 1

    print(start_time_list)
    print(song_title_list)

# Section-3
# call the ffmpeg command to cut each song clip based on start time and end time
# extract audio from the video and save as m4a format
for num in range(count-1):
    print(start_time_list[num] + "\t" + start_time_list[num+1] + "\t" + str(song_title_list[num]))
    os.system("ffmpeg -ss {0} -to {1} -i {2} -c copy {3}.mp4".format(
            start_time_list[num],
            start_time_list[num+1],
            video_path,
            song_title_list[num]
        )
    )
    os.system("ffmpeg -i {0}.mp4 -vn -acodec copy {1}.m4a".format(
        song_title_list[num],
        song_title_list[num]
    ))
