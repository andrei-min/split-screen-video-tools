import ffmpeg
import os

def crop_viewport():
    # decide which folder to work with
    folder = input("[Crop Viewport] " + "Crop viewport from top_videos or bottom_videos folder? ('t' = top, 'b' = bottom): ").lower()
    folder = "./top_videos" if folder == "t" else "./bottom_videos"

    # list files in folder and lets you choose one to work with
    videos = os.listdir(folder)
    print("[Crop Viewport] " + "Files in folder: ")
    index = 0
    for video in videos:
        print("[" + str(index) + "] " + video)
        index += 1
    videoFilename = videos[int(input("[Crop Viewport] " + "Enter index of the video you want crop the viewport: "))]
    print("[Crop Viewport] " + "Selected file: " + videoFilename)

    # ffmpeg probe function returns a dictionary with file info
    info = ffmpeg.probe(str(folder + "/" + videoFilename))

    # check if the video file has audio codec
    has_audio = any(stream["codec_type"] == "audio" for stream in info["streams"])

    # prints video resolution
    print("Video resolution in pixels: " + str(info["streams"][0]["width"]) + " width, " + str(info["streams"][0]["height"]) + " height") 

    # get top-left coordinates of the desired viewport
    print("[Crop Viewport] " + "Starting from the top-left corner of the video (0, 0), enter the coordinates of the viewport, in pixels")
    startW = int(input("start_width pixel: "))
    startH = int(input("start_height_pixel: "))

    # get the height and width of the section you want to keep
    print("[Crop Viewport] " + "Enter the the heigth and width of the section you want to keep, in pixels")
    print("[Crop Viewport] " + "This script will crop down from start_height")
    width = int(input("width: "))
    height = int(input("height: "))

    # get the extension of videoFilename
    extension = os.path.splitext(videoFilename)[1]

    # extract audio first, since ffmpeg filtering seems to remove the audio
    audio = ffmpeg.input(folder + "/" + videoFilename).audio

    # crop the viewport
    croppedVideo = ffmpeg.input(folder + "/" + videoFilename).filter("crop", x=startW, y=startH,  w=width, h=height)

    # add audio back and output the file
    print("[Crop Viewport] " + "Cropping video...")
    print("[Crop Viewport] " + "This may take /a while, depending on the video length and resolution...")

    # add audio back, if any
    if has_audio:
        out = ffmpeg.output(audio, croppedVideo, "{}/{}_croppedViewport{}".format(folder, videoFilename[:-len(extension)], extension)).run()
    else:
        out = ffmpeg.output(croppedVideo, "{}/{}_croppedViewport{}".format(folder, videoFilename[:-len(extension)], extension)).run()

    print("[Crop Viewport] " + "Video cropped successfully")
    print("[Crop Viewport] " + "Output file: " + videoFilename[:-len(extension)] + "_croppedViewport" + extension + " in " + folder)

if __name__ == "__main__":
    crop_viewport()


    