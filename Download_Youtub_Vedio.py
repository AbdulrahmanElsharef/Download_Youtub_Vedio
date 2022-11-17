from pytube import YouTube
from pathlib import Path
from os import *
from pywebio.input import *
from pywebio.output import *


def video_download():
    while True:
        '''function  has one parameter which is the location where to download the file.'''
        video_link = input("Enter YouTube_video link please: ")
        if video_link.split("//")[0] == "https:":
            put_text("video is downloading ..........".title()).style(
                'color: yellow; font-size: 50px')
            # input link of video
            video_url = YouTube(video_link)
            # link of the video to be downloaded
            video = video_url.streams.get_highest_resolution()
            # resolution passed in the get() function
            path_to_download_folder = (r"F:\Download")
            # where to save
            video.download(path_to_download_folder)
            # downloading the video
            put_text("\ndownloading finish  >>>>>>>>>".title()).style(
                'color: blue; font-size: 50px')
            put_text("\nopen file location  >>>>>>>>> ".title()).style(
                'color: green; font-size: 30px')
            # open the video location
            startfile(r"F:\\Download")
        else:
            # invalid link must start with ""https:""
            put_text("invalid YouTube_link\ntry again please".title()).style(
                'color: red; font-size: 50px')


if __name__ == "__main__":
    video_download()

# link="https://www.youtube.com/watch?v=0v54J2ut_LE"

# print(link.split("//")[0])
