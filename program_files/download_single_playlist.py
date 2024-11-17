import os
from program_files.download_single_video import downloadVideosFunction


def downloadSinglePlaylist(playlist, foldername, quality):
    os.system(f"cd playlists && mkdir {foldername}_{quality}")
    for index,url in enumerate(playlist): 
        downloadVideosFunction(url, index, quality, foldername)