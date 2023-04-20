import requests
from bs4 import BeautifulSoup

# 1. 获取用户输入的网址
url = input("请输入网页地址：")

# 2. 获取网页源代码并解析
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 3. 获取音频文件的标题和下载地址
title_tag = soup.find('meta', {'property': 'og:title'})
audio_tag = soup.find('meta', {'property': 'og:audio'})

title = title_tag['content']
audio_url = audio_tag['content']

# 4. 下载音频文件并保存到本地
response = requests.get(audio_url)

with open(f"D:\\{title}.mp3", "wb") as f:
    f.write(response.content)

print(f"音频文件 {title}.mp3 下载完成！")
