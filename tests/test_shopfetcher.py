import unittest
from shopfetcher import *


class TestScraper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skip_all = True

    def test_request(self):
        if self.skip_all:
            self.skipTest("skip")

        sf = ShopFectcher()
        sf.fectch()
        self.assertTrue(True)