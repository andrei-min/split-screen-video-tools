import os
import multiprocessing
import ffmpeg
import json

#function which will split the video
def videoSplit(topVideoFilename, iteration, clipDuration, number, outputFolder):
    #ffmpeg doing the work
    ffmpeg.input(str("./top_videos/" + topVideoFilename), ss = iteration, to = iteration + clipDuration).output(outputFolder + "/clip" + str(number) + ".mp4", loglevel="quiet").run()
    print("[Splitter] " + "Clip " + str(number) + " has been created in " + outputFolder)


def split():
    #top_videos
    #video + audio

    #list files in top_videos folder and lets you choose one to work with
    topVideos = os.listdir("./top_videos")
    print("[Splitter] " + "Files in top_videos folder: ")
    index = 0
    for video in topVideos:
        print("[" + str(index) + "] " + video)
        index += 1
    topVideoFilename = topVideos[int(input("[Splitter] " + "Enter index of bottom video: "))]
    print("[Splitter] " + "Selected file: " + topVideoFilename)

    #ffmpeg probe function returns a dictionary with file info
    info = ffmpeg.probe(str("./top_videos/" + topVideoFilename))

    #prints video duration, as a float
    videoDuration = info["format"]["duration"]
    print("[Splitter] " + "Selected video length: " + videoDuration + " seconds")

    #get the duration of a single clip in which the video will be split, as a str
    clipDuration = input("[Splitter] " + "Enter the duration of a single clip, in seconds: ")

    #because we want the video to be split asap
    print("[Splitter] " + "Video splitting started. expect heavy resource use")
    
    #change values to int in order to work with
    videoDuration = int(float(videoDuration))
    clipDuration = int(float(clipDuration))

    #set outputFolder
    outputFolder = "./top_clips"

    #using the ffmpeg to split the video
    #using multiprocessing to speed up this process

    noWorkers = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(noWorkers)
    number = 0
    for i in range(0, videoDuration, clipDuration):
        pool.apply_async(func=videoSplit, args=(topVideoFilename, i, clipDuration, number, outputFolder))
        number = number + 1

    pool.close()
    pool.join()

    #bottom videos
    #video only

    #list files in top_videos folder and lets you choose one to work with

    bottomVideos = os.listdir("./bottom_videos")
    print("[Splitter] " + "Files in bottom_videos folder: ")
    index = 0
    for video in bottomVideos:
        print("[" + str(index) + "] " + video)
        index += 1
    bottomVideoFilename = bottomVideos[int(input("[Splitter] " + "Enter index of bottom video: "))]
    print("[Splitter] " + "Selected file: " + bottomVideoFilename)

    #ffmpeg probe function returns a dictionary with file info
    info = ffmpeg.probe(str("./bottom_videos/" + bottomVideoFilename))

    #prints video duration, as a float
    videoDuration = info["format"]["duration"]
    print("[Splitter] " + "Selected video length: " + videoDuration + " seconds")

    #get the duration of a single clip in which the video will be split, as a str
    clipDuration = input("[Splitter] " + "Enter the duration of a single clip, in seconds: ")

    #because we want the video to be split asap
    print("[Splitter] " + "Video splitting started. expect heavy resource use")

    #change values to int in order to work with
    videoDuration = int(float(videoDuration))
    clipDuration = int(float(clipDuration))

    #set outputFolder
    outputFolder = "./bottom_clips"

    #using the ffmpeg to split the video
    #using multiprocessing to speed up this process

    noWorkers = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(noWorkers)
    number = 0
    for i in range(0, videoDuration, clipDuration):
        pool.apply_async(func=videoSplit, args=(topVideoFilename, i, clipDuration, number, outputFolder))
        number = number + 1

    pool.close()
    pool.join()

if __name__ == "__main__":
    split()