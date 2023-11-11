import pytube

#function called when a chunk of a video stream has been downloaded.
#prints completion percentage
def downloadProgress(stream, chunk, bytesRemaining):
    fileSize = stream.filesize
    bytesDownloaded = fileSize - bytesRemaining
    percentage = str(round(bytesDownloaded / fileSize * 100, 2))
    print("[Downloader] " + percentage + "%" + " complete", end="\r")

#main download function, to be used in the cli
def youTubeDownload():
    link = input("[Downloader] " + "YouTube video link: ")

    #create YouTube object to work with
    ytObj = pytube.YouTube(link, on_progress_callback=downloadProgress)

    #prints the input to make sure it's a link
    print("\n[Downloader] " +"Video: " + ytObj.title)

    #getting the streams should take a few seconds
    print("\n[Downloader] " + "Getting streams...")
    ytObjStreams = ytObj.streams
    
    #list available streams for download
    #ANDROID_MUSIC streams, as in pytube version 15.0.0
    print("\n[Downloader] "+ "Streams available for download:") 
    for i in ytObjStreams:
        print(i)

    #not every download may work
    print("\n[Downloader] " + "YouTube has no official way for downloading videos or audio files")
    print("[Downloader] " + "You might not find an available stream with your desired characteristics")
    print("[Downloader] " + "The API used in this script may stop working due to YouTube changes")
    print("[Downloader] " + "As a result, this script may be unable to download your file")

    #choose a stream to download
    itag = input("\n[Downloader] " + "Enter the itag of the stream to download: ")
    ytStreamDownload = ytObj.streams.get_by_itag(itag)

    #get, calculate and print duration of the YouTube video
    duration = ytObj.length #in seconds
    durationMinutes = int((duration - (duration % 60)) / 60)
    durationSeconds = int(duration % 60)
    print("\n[Downloader] " +"Stream duration: " + str(durationMinutes) + "m" + str(durationSeconds) + "s")

    #get, calculate and print the file size of the selected stream in megabytes
    filesizeMb = round(ytStreamDownload.filesize / 1e6, 2)
    print("[Downloader] " + "File Size: " + str(filesizeMb) + "mb")

    #starting download; if downloadProgress callback function does not start printing progress, the download may be very slow or not possible at all
    print("\n[Downloader] " + "Downloading stream in ./bottom_videos")
    print("[Downloader] " + "Download may take a while. Make sure to have an uninterrupted internet connection.")
    print("[Downloader] " + "Starting stream download...")
    ytStreamDownload.download("./bottom_videos")

    #download finished
    print("[Downloader] " + "YouTube stream has been downloaded.")
    
#call download function
youTubeDownload()