import requests
from bs4 import BeautifulSoup


def get_dir_name(url, html):
    last = list(filter(None, url.split('/')))[-1]
    link_id = last.split('-')[-1]
    title = html.select_one(".title-section h1").text
    return "data/" + link_id + " - " + title


def get_html(url):
    page_raw = requests.get(url)
    return BeautifulSoup(page_raw.text, 'html.parser')
