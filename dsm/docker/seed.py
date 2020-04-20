import requests

URL = "http://0.0.0.0/controller"


def run():
    x = requests.get(url=URL)


if __name__ == '__main__':
    run()
