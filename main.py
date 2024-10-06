import requests

r = requests.get(
    input("url: "),
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
)

if "yt_ad" in r.text: print("Enabled")
else: print("Disabled")

