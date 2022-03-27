import requests

resp=requests.get("https://video.pearvideo.com/mp4/adshort/20211210/cont-1747603-15804025_adpkg-ad_hd.mp4").content
print(resp)
with open("b.mp4",mode="wb") as f:
    f.write(resp)
print("over")