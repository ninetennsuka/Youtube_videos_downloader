from pytube import YouTube
from moviepy.editor import concatenate_videoclips
import os
import time

# a function to display the video download progress
def progress_function(stream, chunk, bytes_remaining):
    current = ((stream.filesize - bytes_remaining)/stream.filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    print('Downloading: [{}] {}%'.format(status, percent), end='\r')  # display the progress

try:
    url = input("Enter the YouTube URL: ")  

    yt = YouTube(url)
    yt.register_on_progress_callback(progress_function)  # register the progress function

    print("Title: ", yt.title)  # display the title of the video
    print("Views: ", yt.views)  # display the number of views of the video

    print("Available video streams: ")
    video_streams = yt.streams.filter(only_video=True)  # get and display the available video streams
    for i, stream in enumerate(video_streams):
        print(f"{i}. {stream}") 

    stream_number = int(input("Enter the video stream number to download: "))  
    video_stream = video_streams[stream_number]  

    print("Downloading highest available audio stream...")
    audio_stream = yt.streams.get_audio_only()  # get the highest available audio stream

    output_path = input("Enter the path to download the video: ") 

    print("Downloading video...")
    start_time = time.time()
    video_path = video_stream.download(output_path=output_path)  # download the video stream
    print("\nVideo download complete. Time elapsed: " + str(time.time() - start_time))  # display the time elapsed

    print("Downloading audio...")
    start_time = time.time()
    audio_path = audio_stream.download(output_path=output_path)  # download the audio stream
    print("\nAudio download complete. Time elapsed: " + str(time.time() - start_time))  # display the time elapsed

    print("Merging video and audio...")
    video = concatenate_videoclips.VideoFileClip(video_path)  # load the video file
    audio = concatenate_videoclips.AudioFileClip(audio_path)  # load the audio file
    final_output = os.path.join(output_path, "final_output.mp4")
    video.set_audio(audio).write_videofile(final_output)  # merge the video and audio and save the result

    print("Download complete") 
    
except Exception as e:
    print("An error occurred: ", str(e))  # print any errors that occur
