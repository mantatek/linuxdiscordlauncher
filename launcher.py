import requests

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
print(resp)
# with open('thing.tar.gz', 'bw') as file:
#    file.write(resp.read())
print(resp.status_code)
print(resp.headers)
print(resp.reason)

new_url = resp.headers['location']
# f_resp = requests.get(new_url)
# print(f_resp.headers)
# f_resp.close()
resp.close()