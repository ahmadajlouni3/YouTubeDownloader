from pytubefix import YouTube
from pytubefix.cli import on_progress
from program_files.merge_audio_and_video import mergeAudioAndVideo


def downloadVideosFunction(url, index, quality='720p', foldername=None):
    yt = YouTube(url, on_progress_callback = on_progress)
    print(f'Downloading [{index + 1}]: {yt.title}')

    def check_foldername(foldername, index, quality):
        if(foldername):
            mergeAudioAndVideo(index, quality, foldername)
        else:
            mergeAudioAndVideo(index, quality)

    def filter_videos(abr, quality):
        yt.streams.filter(abr=abr, mime_type='audio/mp4')[0].download(filename="test.m4a")
        yt.streams.filter(res=quality, mime_type='video/mp4')[0].download(filename="test.mp4")

    try:
        filter_videos('128kbps', quality)
        check_foldername(foldername, index, quality)
    except:
        filter_videos('48kbps', '480p')
        check_foldername(foldername, index, quality)

print("finish download")

