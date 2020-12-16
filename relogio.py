import requests
from lxml import html
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Accept":"*/*"
}
url="https://www.horariodebrasilia.org/"
page=requests.get(url, headers=headers)
tree=html.fromstring(page.content)
time=tree.xpath('//p[@id="relogio"]/text()')
print(*time)