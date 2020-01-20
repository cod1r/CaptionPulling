import urllib.parse
import requests
import re

videoID = input("Please type the video id here: ")
r = requests.get('https://www.youtube.com/get_video_info?video_id=' + videoID)
chunk = urllib.parse.unquote(r.text)
# urls = re.search
"""
Read regular expressions library for Python and go through all baseUrl links and perform a get request for any possible xml format captions tracks
"""