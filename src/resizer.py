import ffmpeg
import os
import math

def resize():
    # decide which folder to work with
    folder = input("[Resizer] " + "Crop viewport from top_videos or bottom_videos folder? ('t' = top, 'b' = bottom): ").lower()
    folder = "./top_videos" if folder == "t" else "./bottom_videos"

    # list files in folder and lets you choose one to work with
    videos = os.listdir(folder)
    print("[Resizer] " + "Files in folder: ")
    index = 0
    for video in videos:
        print("[" + str(index) + "] " + video)
        index += 1
    videoFilename = videos[int(input("[Crop Viewport] " + "Enter index of the video you want crop the viewport: "))]
    print("[Resizer] " + "Selected file: " + videoFilename)

    # ffmpeg probe function returns a dictionary with file info
    info = ffmpeg.probe(str(folder + "/" + videoFilename))

    print("[Resizer] " + "Detected video resolution: " + str(info["streams"][0]["width"]) + " x " + str(info["streams"][0]["height"]))
    gcd = math.gcd(info["streams"][0]["width"], info["streams"][0]["height"])
    print("[Resizer] " + "Detected aspect ratio: " + str(info["streams"][0]["width"] // gcd) + ":" + str(info["streams"][0]["height"] // gcd))

    print("[Resizer] " + "You can use -1 for width or height to preserve the aspect ratio")
    w = input("[Resizer] " + "Enter desired width: ")
    h = input("[Resizer] " + "Enter desired height: ")

    print("[Resizer] " + "Resizing video...")
    print("[Resizer] " + "This may take a while...")

    extension = os.path.splitext(videoFilename)[1]
    ffmpeg.input(folder + "/" + videoFilename).filter("scale", w, h).output("{}/{}_resized{}".format(folder, videoFilename[:-len(extension)], extension), loglevel="quiet").run()

    print("[Crop Viewport] " + "Video resized successfully")
    print("[Crop Viewport] " + "Output file: " + videoFilename[:-len(extension)] + "_resized" + extension + " in " + folder)

if __name__ == "__main__":
    resize()