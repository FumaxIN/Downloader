# from urllib.request import urlopen
import requests
from urllib.parse import urlparse
from os.path import splitext, basename
import sys
import re
import argparse


class Downloader:

    def __init__(self, parser, args, r, size):
        self.parser = parser
        self.args = args

        self.r = r
        self.size = size

        self.fname = ""

    def f_details(self):
        if 'Content-Disposition' in self.r.headers:
            d = self.r.headers.get('Content-Disposition')
            if "filename" in d:
                file_name_re = re.findall('filename="([^"]*)"', d)[0]
                print("Downloading:", file_name_re)
                self.fname = file_name_re
            else:
                pass
        else:
            split_url = urlparse(self.args.url)
            filename, file_ext = splitext(basename(split_url.path))
            print("Downloading:", filename)

            self.fname = filename

        print("File Size = ", self.size)

    def downloadBar(self):
        dl = 0
        total_length = int(self.size)
        with open(self.fname, 'wb') as file:
            for chunk in self.r.iter_content(10):
                dl += len(chunk)
                file.write(chunk)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                sys.stdout.flush()

        print("\n\n")


p = argparse.ArgumentParser()
p.add_argument('url', type=str)
argss = p.parse_args()
request = requests.get(argss.url, stream=True)
data_size = request.headers['Content-Length']

d = Downloader(p, argss, request, data_size)
d.f_details()
d.downloadBar()
