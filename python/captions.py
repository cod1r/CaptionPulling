import urllib.parse
import requests
import re

videoID = input("Please type the video id here: ")
r = requests.get('https://www.youtube.com/get_video_info?video_id=' + videoID)
chunk = urllib.parse.unquote(r.text)
urls = re.findall(r'/api/timedtext\?(.*?)"', chunk)
for x in range(len(urls)):
    s1 = urls[x].replace('\\u0026', '&')
    s2 = s1.replace(',', "%2C")
    urls[x] = 'https://www.youtube.com/api/timedtext?' + s2
subtitles = []
for x in urls:
    r1 = requests.get(x)
    subtitles.append(r1.text)
for x in range(len(subtitles)):
    bad = re.findall(r'(?=<)(.*?)(?<=>)', subtitles[x])
    for b in range(len(bad)):
        new = subtitles[x].replace(bad[b], "")
        subtitles[x] = new
with open('subtitles.txt', 'wb') as file:
    for x in subtitles:
        file.write(x.encode('utf8'))
        file.write('\n'.encode('utf8'))
