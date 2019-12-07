import unittest
import os
from time import time
from .__main__ import *


class TestScssCompiles(unittest.TestCase):

    def setUp(self):
        self.time = time
        self.path = os.path.join('/tmp', f"website_2018_main_{self.time}.css")

    def test_compile(self):
        compile_scss(os.path.join(ASSETS_DIR, ".."),
                     os.path.join(ASSETS_DIR, "./scss/main.scss"), self.path)
        assert open(self.path, 'r')

    def tearDown(self):
        os.remove(self.path)


if __name__ == '__main__':
    unittest.main()
