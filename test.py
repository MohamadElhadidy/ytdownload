from pytube import YouTube

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(percentage_of_completion)

url = "https://www.youtube.com/watch?v=fO1VIk94ZUw"

# Create the YouTube object first
yt_obj = YouTube(url)

# Then register the callback
yt_obj.register_on_progress_callback(on_progress)
#stream = yt_obj.streams.get_by_itag(17).download()
# Download the video, getting back the file path the video was downloaded to
file_path = yt_obj.streams.filter(progressive=True).get_highest_resolution().download()
print(f"file_path is {file_path}")
#print(yt.title)
#print(yt.author)
#print(yt.caption_tracks)
#print(yt.captions)
#print(yt.channel_id)
#print(yt.channel_url)
#print(yt.check_availability)
#print(yt.description)
#print(yt.fmt_streams)
#print(yt.keywords)
#print(yt.length)
#print(yt.metadata)
#print(yt.publish_date)
#print(yt.rating)
#print(yt.streams)
#print(yt.thumbnail_url)
#print(yt.vid_info)
#print(yt.views)
#print(yt.streaming_data)


