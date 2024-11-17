from pytubefix import Playlist


def input_check(urls_container, folders_name_container, quality):
    type_of_link = input("What you want to download:\n [1] Video\n [2] playlist\n=> ")
    type_of_quality = input("\nchoose quality:\n[1] 1440p60   [2] 1080p60\n[3] 1080p   [4] 720p60\n[5] 720p\n=> ")
    while True:    
        #choose type of link
        if(type_of_link == '1'):
            quality_choose(type_of_quality ,quality)
            confirm_done = singleVideo(urls_container)
            if(confirm_done): break
        elif(type_of_link == '2'):
            quality_choose(type_of_quality ,quality)
            confirm_done = playlistDownload(urls_container, folders_name_container)
            if(confirm_done): break
        #if check good
        else:
            print("please enter number between 1 or 2!")
            break




#download single video
def singleVideo(urls_container):
    try:
        url = input("Video_url=> ")
        urls_container.append(url)
        return True
    except:
        print("please enter valid url!")
        return False


#download playlist
def playlistDownload(urls_container, folders_name_container):
    try:
        url = input("playlist_url=> ")
        folder_name = input("What is name of folder for this playlist: ")
        if(folder_name):
            confirm = input("Do you need add more playlist links? (Y/N) ")
            folders_name_container.append(folder_name)
            if(confirm == "y" or confirm == "Y"):
                urls_container.append(Playlist(url))
            elif (confirm == "n" or confirm == "N" and folder_name):
                urls_container.append(Playlist(url))
                return True
            else:
                print("please enter correct answer!")
        else:
            print("please enter the name of the file!")
    except:
        print("please enter valid url!")
    

#quality choose
def quality_choose(type_quality ,quality_container):
    if(type_quality == '1'):
        quality_container.append('1440p60')
    elif(type_quality == '2'):
        quality_container.append('1080p60')
    elif(type_quality == '3'):
        quality_container.append('1080p')
    elif(type_quality == '4'):
        quality_container.append('720p60')
    elif(type_quality == '5'):
        quality_container.append('720p')
    else:
        print("please enter valid answer!")