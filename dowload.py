# from urllib.request import urlopen
import requests
# with urlopen("http://www.sampledocs.in/DownloadFiles/SampleFile?filename=sampledocs-%20dummy%20Video&ext=mp4") as video:
#     with open("video1.mp4", "w") as new_file:
#         for chunk in video.iter_content(chunk_size=10):
#             new_file.write(chunk)

r = requests.get("http://www.sampledocs.in/DownloadFiles/SampleFile?filename=sampledocs-%20dummy%20Video&ext=mp4", stream=True)
with open("video_from_requests", 'wb') as file:
    for chunk in r.iter_content(10):
        file.write(chunk)