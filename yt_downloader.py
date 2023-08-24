from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=LjcuNZ9lU90")

yd = yt.streams.get_highest_resolution()

yd.download()
print("video downloaded")
