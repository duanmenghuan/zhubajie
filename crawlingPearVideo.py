import requests
url = "https://www.pearvideo.com/video_1749901"
contId = url.split("_")[1]
videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}"

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
'Referer': url
}

req = requests.get(url=videoStatusUrl,headers=headers)
dic = req.json()
srcUrl = dic["videoInfo"]['videos']['srcUrl']
systemTime =dic['systemTime']
srcUrl = srcUrl.replace(systemTime,f"cont-{contId}")

with open("a.mp4",mode ="wb") as f:
    f.write(requests.get(srcUrl).content)
