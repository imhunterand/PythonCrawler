import unittest
from src.crawler import WebCrawler

class TestWebCrawler(unittest.TestCase):

    def test_crawl(self):
        crawler = WebCrawler("https://example.com", max_pages=1)
        crawler.run()
        self.assertGreater(len(crawler.data), 0)

if __name__ == '__main__':
    unittest.main()
