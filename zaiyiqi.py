import re
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

last = 1613708132614
cursor = '0'
content_list = []

for i in range(1000):
    url = "https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" + cursor + "&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_="+str(last)
    source = requests.get(url, headers=headers).content.decode()
    result = re.findall('"content":"(.*?)","up"', source, re.S)
    content_list.append(result)
    cursor = re.findall('"last":"(.*?)","', source, re.S)[0]

with open("content.txt", "w", encoding="utf-8", errors="ignore") as f:
    for i in content_list:
        for j in i:
            f.write(j)
            f.write("\n")


