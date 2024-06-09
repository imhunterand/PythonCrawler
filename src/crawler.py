from src.utils import get_page_content, is_valid_url, can_fetch
from src.parser import extract_links, extract_title, extract_content
from src.storage import save_to_csv
import time

class WebCrawler:
    def __init__(self, start_url, max_pages=50):
        self.start_url = start_url
        self.max_pages = max_pages
        self.visited = set()
        self.data = []

    def crawl(self, url):
        if len(self.visited) >= self.max_pages:
            return
        if url in self.visited:
            return
        if not is_valid_url(url):
            return
        if not can_fetch(url):
            return

        print(f"Crawling: {url}")
        content = get_page_content(url)
        self.visited.add(url)

        title = extract_title(content)
        page_content = extract_content(content)
        links = extract_links(content, self.start_url)

        self.data.append({
            'url': url,
            'title': title,
            'content': page_content
        })

        for link in links:
            self.crawl(link)

    def run(self):
        self.crawl(self.start_url)
        save_to_csv(self.data)

if __name__ == "__main__":
    start_url = input("Enter the URL of the website to crawl: ")
    crawler = WebCrawler(start_url)
    crawler.run()
