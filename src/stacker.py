import ffmpeg
import os

def stack():
    # choose top video
    print("[Stacker] " + "Choose the top video: ")
    folder = "./top_videos"
    videos = os.listdir(folder)
    print("[Stacker] " + "Files in folder: ")
    index = 0
    for video in videos:
        print("[" + str(index) + "] " + video)
        index += 1
    topVideoFilename = videos[int(input("[Stacker] " + "Enter index of the top video: "))]
    print("[Resizer] " + "Selected file: " + topVideoFilename)

    # choose bottom video
    print("[Stacker] " + "Choose the bottom video: ")
    folder = "./bottom_videos"
    videos = os.listdir(folder)
    print("[Stacker] " + "Files in folder: ")
    index = 0
    for video in videos:
        print("[" + str(index) + "] " + video)
        index += 1
    bottomVideoFilename = videos[int(input("[Stacker] " + "Enter index of the bottom: "))]
    print("[Stacker] " + "Selected file: " + bottomVideoFilename)

    topVideo = ffmpeg.input("./top_videos/" + topVideoFilename)
    bottomVideo = ffmpeg.input("./bottom_videos/" + bottomVideoFilename)

    extension = os.path.splitext(topVideoFilename)[1]
    print("[Stacker] " + "Generating stacked video...")
    out = ffmpeg.filter([topVideo, bottomVideo], "vstack").output(topVideo, bottomVideo, "{}/{}_stacked{}".format(folder, topVideoFilename[:-len(extension)], extension)).run()

    print("[Stacker] " + "Videos stacked successfully")
    print("[Stacker] " + "Output file: " + topVideoFilename[:-len(extension)] + "_stacked" + extension + " in " + folder)

if __name__ == "__main__":
    stack()