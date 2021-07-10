from pytube import YouTube
import requests
import re


def fetch(url):
    html = requests.get(url, timeout=5)
    regex = r'watch\?v=[a-zA-Z0-9_.-]*'
    videoLinks = re.findall(regex, html.text)
    print(videoLinks)
    for link in videoLinks:
        youtubeDownload(link)


def youtubeDownload(url):
    print('checking')
    yt = YouTube('https://www.youtube.com/'+url)
    print("Title: ", yt.title)
    print("Number of views: ", yt.views)
    print("Length of video: ", yt.length, "seconds")
    print("Rating of video: ", yt.rating)
    ys = yt.streams.get_highest_resolution()
    # Starting download
    print("Downloading...")
    ys.download()
    print("Download completed!!")


fetch(input('page url with youtube content: '))
