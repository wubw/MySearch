import unittest
import crawler

class TestCrawler(unittest.TestCase):
    def test_start(self):
        c = crawler.Crawler()
        c.start()
        self.assertGreater(c.files_cnt, 500)
        self.assertIn('.md', c.ext_check)
        self.assertIn('.txt', c.ext_check)

if __name__ == '__main__':
    unittest.main()