import requests

# GET, POST

url = 'https://random-d.uk/api/random'


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