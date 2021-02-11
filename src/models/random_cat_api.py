import requests


class RandomCatApi:
    def __init__(self):
        self.url = "https://aws.random.cat/meow"

    def get_cat_img(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json().get("file")
        raise RuntimeError("Sorry... 40cat not found!")
