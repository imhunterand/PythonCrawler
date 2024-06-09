from bs4 import BeautifulSoup

def extract_links(html, base_url):
    soup = BeautifulSoup(html, 'lxml')
    links = []
    for link in soup.find_all('a', href=True):
        url = link['href']
        if not url.startswith('http'):
            url = base_url + url
        links.append(url)
    return links

def extract_title(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup.title.string if soup.title else "No Title"

def extract_content(html):
    soup = BeautifulSoup(html, 'lxml')
    paragraphs = soup.find_all('p')
    return "\n".join([p.get_text() for p in paragraphs])
