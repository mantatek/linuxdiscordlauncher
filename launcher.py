import requests
import os
import urllib.parse
import tarfile
import subprocess

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
resp.close()

print(file_url)
path = urllib.parse.urlparse(file_url).path
# e.g. /apps/linux/0.0.32/discord-0.0.32.tar.gz
path_segments = path.split("/")
file_name = path_segments[-1]
version = path_segments[-2]
new_upd = False
extracted = "./files/%s"%version
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
    archive = "./files/%s"%file_name
    with open(archive, 'bw') as file:
        file.write(f_resp.content)
    with tarfile.open(archive) as tar:
        tar.extractall(extracted)
    f_resp.close()
else:
    print("no new update, starting discord")

disc_exe = "%s/Discord/Discord"%extracted
input("About to run executable file %s; press ENTER to continue, CTRL-C to quit"%disc_exe)
subprocess.run(disc_exe)