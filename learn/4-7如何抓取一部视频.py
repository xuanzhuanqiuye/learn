import time
import requests

# m3u8url="https://e1.monidai.com/ppvod/FFF726E1004D71179AABE86440FDCFCA.m3u8"
# #下载m3u8
n=1
# resp=requests.get(m3u8url)
# with open("谎言真探.m3u8",mode="wb") as f:
#     f.write(resp.content)
# resp.close()
headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95"
    }
with open("谎言真探.m3u8",mode="r",encoding="utf-8") as f:
    for line in f:
        line=line.strip()
        if line.startswith("#"):
            continue
        print(line)
        time.sleep(0.5)
        resp1=requests.get(line,headers=headers)
        f=open(f"video/{n}.ts",mode="wb")
        f.write(resp1.content)
        n+=1
        resp1.close()
        print("over!",n)
print("over!")
