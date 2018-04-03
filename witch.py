import requests
from bs4 import BeautifulSoup
import re


def fetch_html(url):
    print(url)
    res = requests.get(url)
    if res.status_code == 200:
        return res.content.decode('utf-8')
    else:
        return '<html></html>'


def parse(body):
    t = body.split('doreq();')[0].strip()
    return t.split('ＷＩＴＣＨ？')[1].strip()


def fetch_info():
    base_uri = 'http://witch.valdikss.org.ru/'
    endpoint = base_uri
    html = fetch_html(endpoint)
    soup = BeautifulSoup(html)
    body = soup.body.text.strip()
    parsed_body = parse(body)
    return parsed_body


if __name__ == '__main__':
    fetch_info()
