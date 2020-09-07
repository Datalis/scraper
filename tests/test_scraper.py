import unittest
from scraper import *


class TestScraper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skip_all = True

    def test_load(self):
        if self.skip_all:
            self.skipTest("skip")

        scraper = Scraper()
        html = "<html></html>"
        self.assertIsNone(scraper.get_html())
        scraper.load(html, DataType.Html)
        self.assertEqual(scraper.get_html(), html)

    def  test_get_html(self):
        if self.skip_all:
            self.skipTest("skip")

        scraper = Scraper()
        url = "https://fileinfo.com/list/1"
        scraper.load(url, DataType.Url)
        self.assertIsNotNone(scraper.get_html())





