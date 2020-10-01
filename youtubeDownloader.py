import pytube


url = 'https://www.youtube.com/watch?v=aF3MrOds984'
youtube = pytube.YouTube(url)
video = youtube.streams.get_by_itag(135)
video.download('C:/Users/Administrator/Desktop')
print('done')

# streams = youtube.streams.all()
# for i in streams:
#     print(i)