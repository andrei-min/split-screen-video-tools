import ffmpeg
import os

def trimmer():

    #decide which folder to work with
    folder = input("[Trimmer] " + "Trim video from top_videos or bottom_videos folder? ('t' = top, 'b' = bottom): ").lower()
    folder = "./top_videos" if folder == "t" else "./bottom_videos"

    #list files in folder and lets you choose one to work with
    videos = os.listdir(folder)
    print("[Trimmer] " + "Files in folder: ")
    index = 0
    for video in videos:
        print("[" + str(index) + "] " + video)
        index += 1
    videoFilename = videos[int(input("[Trimmer] " + "Enter index of the video you want to trim: "))]
    print("[Trimmer] " + "Selected file: " + videoFilename)
    
    #get start and end time
    start = input("[Trimmer] " + "Where should the trimming start? (hh:mm:ss): ")
    end = input("[Trimmer] " + "Where should the trimming end? (hh:mm:ss): ")

    #trim the video
    print("[Trimmer] " + "Trimming video...")
    print("[Trimmer] " + "Expect heavy resource use")

    #get the extension of videoFilename
    extension = os.path.splitext(videoFilename)[1]

    #trim the video
    ffmpeg.input(folder + "/" + videoFilename, ss=start, to=end).output(folder + "/" + videoFilename[:-len(extension)] + "_trimmed" + extension, loglevel="quiet").run()
    print("[Trimmer] " + "Video trimmed successfully")
    print("[Trimmer] " + "Output file: " + videoFilename[:-len(extension)] + "_trimmed" + extension + " in " + folder)

if __name__ == "__main__":
    trimmer()