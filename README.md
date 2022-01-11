# Downloader

Downloader is a simple python script that can download any file from a given URL

## Running

#### Requirements

* [Python](https://www.python.org/downloads/)

#### Steps
Download the file

```shell
git clone https://github.com/FumaxIN/Downloader.git
```
Switch to the directory
```shell
cd Downloader
```
Run the command
```shell
python downloader.py "[Download Link]"
```

## How it works

* Accpts the URL with `argparse`
    
* Streams the URL
    
* Checks for `filename` in Headers with regex OR extracts from URL if unable to find in headers.
    
* Extracts Download Size from Headers.
    
* Download Progress Bar for interactive update.
    
* File is downloaded.
