# from urllib.request import urlopen
import requests
from urllib.parse import urlparse
from os.path import splitext, basename
import sys
import re
# with urlopen("http://www.sampledocs.in/DownloadFiles/SampleFile?filename=sampledocs-%20dummy%20Video&ext=mp4") as video:
#     with open("video1.mp4", "w") as new_file:
#         for chunk in video.iter_content(chunk_size=10):
#             new_file.write(chunk)

url = str(input("Paste the URL to download a file: "))
r = requests.get(url, stream=True)

if 'Content-Disposition' in r.headers:
    d = r.headers.get('Content-Disposition')
    file_name_re = re.findall('filename=(.+)', d)[0]
    print(file_name_re)

else:
    split_url = urlparse(url)
    filename, file_ext = splitext(basename(split_url.path))
    output = str(filename+file_ext)
    print("Filename = ", filename)

size = r.headers['Content-Length']
print("Visiting URL: ", url)
print("File Size = ", size)


dl = 0
total_length = int(size)
with open("sample1", 'wb') as file:
    for chunk in r.iter_content(10):
        dl += len(chunk)
        file.write(chunk)
        done = int(50 * dl / total_length)
        sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
        sys.stdout.flush()
