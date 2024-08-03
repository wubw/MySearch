import unittest
import pre_processor

class TestPreProcessor(unittest.TestCase):
    ppr = pre_processor.PreProcessor()

    def test_remove_newlines(self):
        with open('test_data/test_url.txt', 'r') as file:
            working_txt = file.read()
            self.assertEqual(working_txt.count('\n'), 9)

            clean_text = self.ppr.remove_newline(working_txt)
            self.assertEqual(clean_text.count('\n'), 0)

    def test_remove_url(self):
        with open('test_data/test_url.txt', 'r') as file:
            working_txt = file.read()
            self.assertEqual(working_txt.count('http'), 3)

            clean_text = self.ppr.remove_urls(working_txt)
            self.assertEqual(clean_text.count('http'), 0)

    def test_aggregate(self):
        with open('test_data/Null POI.md', 'r') as file:
            working_txt = file.read()
            self.assertEqual(working_txt.count('http'), 13)

            clean_text = self.ppr.remove_urls(working_txt)
            self.assertEqual(clean_text.count('http'), 0)

            self.assertEqual(clean_text.count('\n'), 46)
            clean_text = self.ppr.remove_newline(clean_text)
            self.assertEqual(clean_text.count('\n'), 0)

            print(clean_text)

if __name__ == '__main__':
    unittest.main()
