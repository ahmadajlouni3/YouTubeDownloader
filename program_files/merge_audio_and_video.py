import os


def mergeAudioAndVideo(index, quality, foldername=None):
    if(foldername):
        os.system(f"cd converter && ffmpeg -i ../test.mp4 -i ../test.m4a -c copy -map 0:v:0 -map 1:a:0 ../playlists/{foldername}_{quality}/output-{index}.mp4")
    else:
        os.system(f"cd converter && ffmpeg -i ../test.mp4 -i ../test.m4a -c copy -map 0:v:0 -map 1:a:0 ../playlists/output-{index}.mp4")
    os.system("rm test.m4a test.mp4")
    os.system("clear")
