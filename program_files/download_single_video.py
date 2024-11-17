from pytubefix import YouTube
from pytubefix.cli import on_progress
from program_files.merge_audio_and_video import mergeAudioAndVideo


def downloadVideosFunction(url, index, quality='720p', foldername=None):
    count = index
    yt = YouTube(url, on_progress_callback = on_progress)
    videoName = yt.title
    print(f'Downloading [{count}]: {videoName}')
    
    try:
        yt.streams.filter(abr='128kbps', mime_type='audio/mp4')[0].download(filename="test")
        yt.streams.filter(res=quality, mime_type='video/mp4')[0].download(filename="test")
        if(foldername):
            mergeAudioAndVideo(index, quality, foldername)
        else:
            mergeAudioAndVideo(index, quality)

        print("finish download")
    except:
        print("the video don't have quality like what you choose, we will download video with 720p quality")
        yt.streams.filter(abr='48kbps', mime_type='audio/mp4')[0].download(filename="test")
        yt.streams.filter(res="480p", mime_type='video/mp4')[0].download(filename='test')
        if(foldername):
            mergeAudioAndVideo(index, quality, foldername)
        else:
            mergeAudioAndVideo(index, quality)

        print("finish download")

