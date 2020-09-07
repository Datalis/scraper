import unittest
from filetype_scraper import *

class TestFiletypeScraper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skip_all = True

    def test_get_filetype_links(self):
        if self.skip_all:
            self.skipTest("skip")

        f_scraper = FiletypeScraper()
        url = "https://fileinfo.com/list/1"
        f_scraper.load(url, DataType.Url)
        f_links = f_scraper.get_filetype_links()
        self.assertEqual(len(f_links), 183)

    def test_get_sources(self):
        if self.skip_all:
            self.skipTest("skip")

        f_scraper = FiletypeScraper()
        url = "https://fileinfo.com/list/1"
        f_scraper.load(url, DataType.Url)
        sources = f_scraper.get_sources()
        self.assertTrue(sources[0].startswith("https://fileinfo.com/list"))

    def test_parse_extension_info(self):
        if self.skip_all:
            self.skipTest("skip")

        f_scraper = FiletypeScraper()

        ext_link = 'https://fileinfo.com/extension/!bt'

        description_expected = {
            'filetype': '.!bt',
            'developer': 'BitTorrent',
            'category': 'Misc Files',
            'format': 'Text and Binary'
        }
        description_result = f_scraper.parse_extension(ext_link, DataType.Url)

        self.assertEqual(description_result, description_expected)


