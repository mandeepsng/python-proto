from pytube import YouTube

ask = input('Enter url => ')
print(ask)
yt = YouTube(ask)
vid = yt.streams.filter(progressive=True, file_extension='mp4').desc().first().download('')





