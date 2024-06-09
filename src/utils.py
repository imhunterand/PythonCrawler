import requests
from bs4 import BeautifulSoup
import time

def get_page_content(url):
    response = requests.get(url)
    time.sleep(1)  # Menambahkan jeda untuk menghindari pemblokiran
    return response.text

def parse_html(content):
    return BeautifulSoup(content, 'lxml')

def is_valid_url(url):
    return url.startswith("http")

def get_robots_txt(url):
    robots_url = url + "/robots.txt"
    try:
        response = requests.get(robots_url)
        if response.status_code == 200:
            return response.text
    except requests.exceptions.RequestException:
        pass
    return ""

def can_fetch(url, user_agent='*'):
    robots_txt = get_robots_txt(url)
    for line in robots_txt.split('\n'):
        if line.startswith('User-agent:'):
            if user_agent in line or '*' in line:
                continue
        if line.startswith('Disallow:'):
            path = line.split(':')[1].strip()
            if url.startswith(path):
                return False
    return True
