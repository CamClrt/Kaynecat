import requests


class KanyeRestApi:
    def __init__(self):
        self.url = "https://api.kanye.rest"

    def get_kanye_quote(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json().get("quote")
        raise RuntimeError("Sorry... Kanye lost his voice!")
