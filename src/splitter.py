import os
import multiprocessing
import ffmpeg
import json

#function which will split the video
def videoSplit(bottomVideoFilename, iteration, clipDuration, number):
    ffmpeg.input(str("./bottom_videos/" + bottomVideoFilename), ss = iteration, to = iteration + clipDuration).output("clip" + str(number) + ".mp4", loglevel="quiet").run()
    print("Clip " + str(number) + " has been created.")


#top video
#video + audio

# topVideos = os.listdir("./topVideos")
# print("Files in topVideos folder: ")
# index = 0
# for i in topVideos:
#     print("[" + str(index) + "] " + i)
#     index += 1

# topVideoFilename = topVideos[int(input("Enter index of top video: "))]
# print("Selected file: " + topVideoFilename)
# print(str("./topVideos/" + topVideoFilename))
# info = ffmpeg.probe(str("./topVideos/" + topVideoFilename))

# for debugging
# print(info)
# print(json.dumps(info, indent = 5))

# print("Selected video length: " + info["format"]["duration"] + " seconds")


#bottom videos

#list files in bottom_videos folder and lets you choose one to work with
bottomVideos = os.listdir("./bottom_videos")
print("Files in bottom_videos folder: ")
index = 0
for video in bottomVideos:
    print("[" + str(index) + "] " + video)
    index += 1
bottomVideoFilename = bottomVideos[int(input("Enter index of bottom video: "))]
print("Selected file: " + bottomVideoFilename)

#ffmpeg probe function returns a dictionary with file info
info = ffmpeg.probe(str("./bottom_videos/" + bottomVideoFilename))

#prints video duration, as a float
videoDuration = info["format"]["duration"]
print("Selected video length: " + videoDuration + " seconds")

#get the duration of a single clip in which the video will be split, as a str
clipDuration = input("Enter the duration of a single clip, in seconds: ")

#change values to int in order to work with
videoDuration = int(float(videoDuration))
clipDuration = int(float(clipDuration))

#using the ffmpeg to split the video
#using multiprocessing to speed up this

noWorkers = multiprocessing.cpu_count()
pool = multiprocessing.Pool(noWorkers)
number = 0
for i in range(0, videoDuration, clipDuration):
    pool.apply_async(func=videoSplit, args=(bottomVideoFilename, i, clipDuration, number))
    number = number + 1

pool.close()
pool.join()