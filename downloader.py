# from urllib.request import urlopen
import requests
from urllib.parse import urlparse
from os.path import splitext, basename
import sys
import re
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('url', type=str)
args = parser.parse_args()


r = requests.get(args.url, stream=True)

fname = ""

if 'Content-Disposition' in r.headers:
    d = r.headers.get('Content-Disposition')
    pattern = re.compile('filename=(.+)')
    if "filename" in d:
        file_name_re = re.findall('filename="([^"]*)"', d)[0]
        print(file_name_re)

        fname = file_name_re
    else:
        split_url = urlparse(args.url)
        filename, file_ext = splitext(basename(split_url.path))
        output = str(filename+file_ext)
        print("Filename = ", filename)

        fname = filename

size = r.headers['Content-Length']
print("Visiting URL: ", args.url)
print("File Size = ", size)


dl = 0
total_length = int(size)
with open(fname, 'wb') as file:
    for chunk in r.iter_content(10):
        dl += len(chunk)
        file.write(chunk)
        done = int(50 * dl / total_length)
        sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
        sys.stdout.flush()

print("\n\n")