import os
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOADS_DIR = os.path.join(BASE_DIR, 'downloads')
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

img_path = os.path.join(DOWNLOADS_DIR, 'corgi.jpg')

url = "https://i.pinimg.com/originals/2a/e9/a4/2ae9a40b4363e74554dcae603cd8356d.jpg"

r =requests.get(url, stream=True)
r.raise_for_status()

with open(img_path, 'wb') as f:
    f.write(r.content)