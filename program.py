from program_files.input_check import input_check
from program_files.download_single_playlist import downloadSinglePlaylist
from program_files.download_single_video import downloadVideosFunction


urls = []
folders_name = []
quality = []

print(f'''
{'='*65}
{' '*20} Welcome To Youtube Downloader
{'='*65}
''')

print("Builded by ( ahmadajlouni3 )")
print("github: @ahmadajlouni3")
print("linkedin: www.linkedin.com/in/ahmad-alajlouni-1ab9a820a\n\n")


#input collector and checker
input_check(urls, folders_name, quality)


try:
    if(len(urls) == 1 and len(folders_name) == 0):
        downloadVideosFunction(urls[0], 1, quality[0])
    else:
        for index, playlist in enumerate(urls):
            downloadSinglePlaylist(playlist, folders_name[index], quality[0])
except:
    print("somthing error: expect from inputs")



print("Playlist Downloaded Complete\n")

print("I have also alot of upgrade to this program that coming soon like:")
print("convert it to gui")
print("add other features like auto quality detection")
print("insert name to downloaded file and support many language\n")

print("you can donate me from this wallet (usdt-trc20)\n")
print('( TAxfquoA3qgfYTCv5NGACPCQngPR46qUFY )')
