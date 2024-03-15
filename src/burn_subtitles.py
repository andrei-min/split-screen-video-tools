import os
import ffmpeg

def burn_subtitles():

    # decide which folder to work with
    folder = input("[Burn Subtitles] " + "Select video file from top_videos or bottom_videos folder? ('t' = top, 'b' = bottom): ").lower()
    folder = "./top_videos" if folder == "t" else "./bottom_videos"

    # list files in folder and lets you choose one to work with
    videos = os.listdir(folder)
    print("[Burn Subtitles] " + "Files in folder: ")
    index = 0
    for video in videos:
        print("[" + str(index) + "] " + video)
        index += 1
    videoFilename = videos[int(input("[Burn Subtitles] " + "Enter index of the video you want burn subtitles to: "))]
    print("[Burn Subtitles] " + "Selected file: " + videoFilename)
    
    original = ffmpeg.input(folder + "/" + videoFilename)
    # ffmpeg probe function returns a dictionary with file info
    info = ffmpeg.probe(str(folder + "/" + videoFilename))

    # tterate over each stream and check if it is a subtitle stream
    subtitles = [stream for stream in info['streams'] if stream['codec_type'] == 'subtitle']

    if not subtitles:
        print("[Burn Subtitles] No subtitles found in the video.")
    else:
        print("[Burn Subtitles] Subtitles found in the video:")
        for i, stream in enumerate(subtitles):
            title = stream.get('tags', {}).get('language', 'Unknown')
            print("[{}]: {}".format(i, title))
    
    subIndex= input("[Burn Subtitles] Choose the subtitle stream index to burn: ")
    
    extension = os.path.splitext(videoFilename)[1]

    print("[Burn Subtitles] " + "Burning subtitles...")
    out = ffmpeg.output(original,  "{}/{}_subtitled{}".format(folder, videoFilename[:-len(extension)], extension), vf="subtitles={}:si={}".format(folder + "/" + videoFilename, subIndex)).run()

    print("[Burn Subtitles] " + "Subtitles burned successfully")
    print("[Burn Subtitles] " + "Output file: " + videoFilename[:-len(extension)] + "_subtitled" + extension + " in " + folder)

if __name__ == "__main__":
    burn_subtitles()
