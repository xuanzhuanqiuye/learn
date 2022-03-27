#拿到contid
#拿道videostatus返回得json——》srcURL
#srcURL里面得内容进行休整
#下载视频
import requests

url="https://www.pearvideo.com/video_1747603"
contid=url.split("_")[1]
videoStatusUrl=f"https://www.pearvideo.com/videoStatus.jsp?contId={contid}&mrd=0.815340467403265"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
    "Referer":"https://www.pearvideo.com/video_1747603"

}
resp=requests.get(videoStatusUrl,headers=headers)
dic=resp.json()
srcUrl=dic["videoInfo"]["videos"]["srcUrl"]
print(srcUrl)
systemTime=dic["systemTime"]
#假链接https://video.pearvideo.com/mp4/third/20211112/1639221904202-11905134-084204-hd.mp4
#真链接https://video.pearvideo.com/mp4/third/20211112/cont-1745727-11905134-084204-hd.mp4
#https://video.pearvideo.com/mp4/adshort/20211210/cont-1747603-15804025_adpkg-ad_hd.mp4
srcUrl=srcUrl.replace(systemTime,f"cont-{contid}")
print(srcUrl)
#下载视频

resp1=requests.get(srcUrl).content
print(resp1)
with open("a.mp4",mode="wb") as f:
    f.write(resp1)

print("over")