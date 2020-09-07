import unittest
from headless import *

class TestHeadless(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skip_all = False

    def test_take_screenshot(self):
        if self.skip_all:
            self.skipTest("skip")

        headless = HeadlessChrome()
        headless.take_screenshot("http://dondehay.cimex.com.cu/")

        self.assertTrue(True)