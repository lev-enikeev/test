import requests
import torch
from torchvision import models
import torch.nn as nn
import numpy as np
import cv2
# GET, POST

url = 'https://random-d.uk/api/random'

model = models.resnet50(pretrained=False)
model.fc = nn.Sequential(
    nn.Linear(2048, 128),
    nn.ReLU(inplace=True),
    nn.Linear(128, 1),
    nn.Sigmoid())
model.load_state_dict(torch.load('weights.h5'))
model = model.eval()


def load_image(path):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (560, 560))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB).astype(np.float32)
    img /= 255.
    img = torch.from_numpy(img).permute(2, 0, 1)
    img = img.unsqueeze(0)
    return img


def predict_img(img_path):
    img = load_image(img_path)
    res = float(model(img)[0][0])
    if res > 0.5:
        return 'HOT DOG'
    return 'PROBABLY NOT A HOT DOG'


def random_dog():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    res = res.json()
    return res['url']


def random_duck():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    res = res.json()
    return res['url']


def random_anime(category):
    url = f'https://api.waifu.pics/sfw/%7Bcategory%7D'
    res = requests.get(url)
    res = res.json()
    return res['url']


def run_code_api(code):
    payload = {
        "version": "3.10.0",
        'language': 'python3',
        "files": [
            {
                "content": code
            }
        ],
    }
    url = 'https://emkc.org/api/v2/piston/execute'
    res = requests.post(
        url, headers={'Content-Type': 'application/json'}, json=payload)
    data = res.json()
    if 'message' in data:
        return 'Данные не похожи на питоновский код'
    return data['run']['stdout']
