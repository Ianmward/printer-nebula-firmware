from bs4 import BeautifulSoup
import requests
import re

url = "https://www.creality.com/pages/download-creality-nebula-smart-kit"
firmware_link_re = re.compile(r"https://file2-cdn\.creality\.com/file/[A-Za-z0-9]+/NEBULA_ota_img_V(\d+\.\d+\.\d+\.\d+)\.img")

req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")

tags = soup.find_all('a')

links = []
for tag in tags:
    if not tag.get('href'):
        continue
    links.append(tag['href'])

firmware_links = [
    m.group(1)
    for link in links
    if (m := firmware_link_re.match(link))
]

if not firmware_links:
    print("Error: No firmware links found.")
    exit(1)

print(sorted(firmware_links)[-1])