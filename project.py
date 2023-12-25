from pytube import YouTube
from sys import argv

# Check if the script is provided with a command-line argument
if len(argv) < 2:
    print("Usage: python script_name.py <YouTube_video_URL>")
    exit(1)

# Get the YouTube video URL from the command-line argument
link = argv[1]

try:
    yt = YouTube(link)
    print("Title: ", yt.title)
    print("Views: ", yt.views)

    # Get the highest resolution stream
    yd = yt.streams.get_highest_resolution()

    # Download the video
    yd.download(r'C:\Users\jenis\Desktop\YT Download')

except Exception as e:
    print(f"An error occurred: {e}")
