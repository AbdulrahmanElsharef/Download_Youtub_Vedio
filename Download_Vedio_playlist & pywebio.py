from pytube import YouTube
from pytube import Playlist
from os import *
from pywebio.input import *
from pywebio.output import *


def video_download_playlist():
    while True:
        SAVE_PATH = (r"F:\\Download\\youtup")  # pasth to save videos
        # link of the video to be downloaded
        videos_links = input("Enter YouTube_Playlist links please: ".title())
        # put all links into playlist funcion
        playlist = Playlist(videos_links)
        # get all urls in playlist
        PlayListLinks = playlist.video_urls
        # get number of links of playlist
        num = len(PlayListLinks)
        # print('Number of videos in playlist len(PlayListLinks))
        put_text(f"number of Playlist Links is {num} videos ".title()).style(
            'color: green; font-size: 50px')
        put_text(f"\n Lets Download all {num} videos >>>>>>".title()).style(
            'color: yellow; font-size: 50px')
        for i, link in enumerate(PlayListLinks):
            yt = YouTube(link)
            d_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by(
                'resolution').desc().first()
            d_video.download(SAVE_PATH)
            put_text(i+1, ' Video is Downloaded .....'.title()).style(
                'color: blue; font-size: 50px')


if __name__ == "__main__":
    video_download_playlist()


