import requests
import os
import urllib.parse

GET_URL = "https://discord.com/api/download"
params = {
    "platform": "linux",
    "format": "tar.gz"
}

# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Connection": "keep-alive",
#     "Upgrade-Insecure-Requests": "1"
# }


resp = requests.get(GET_URL, params=params, allow_redirects=False)
# with open('thing.tar.gz', 'bw') as file:
#    file.write(resp.read())

file_url = resp.headers['location']
print(file_url)
path = urllib.parse.urlparse(file_url).path
# e.g. /apps/linux/0.0.32/discord-0.0.32.tar.gz
path_segments = path.split("/")
file_name = path_segments[-1]
version = path_segments[-2]
new_upd = False
with open("version.txt") as versionfile:
    oldv = versionfile.read()
if oldv != version:
    new_upd = True
    with open("version.txt", 'w') as versionfile:
        versionfile.write(version)

if new_upd:
    print("new update available, download beginning...")
    f_resp = requests.get(file_url)
    if not os.path.exists("./files/"):  
       os.mkdir("files")
    with open("files/%s"%file_name, 'bw') as file:
        file.write(f_resp.content)
    f_resp.close()
else:
    print("no new update, starting discord")
resp.close()