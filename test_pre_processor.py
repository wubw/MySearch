import unittest
import pre_processor

class TestPreProcessor(unittest.TestCase):

    def test_remove_newlines(self):
        ppr = pre_processor.PreProcessor('test_data/test_url.txt')
        self.assertEqual(ppr.working_txt.count('\n'), 9)
        ppr.remove_newline()
        self.assertEqual(ppr.working_txt.count('\n'), 0)

    def test_remove_url(self):
        ppr = pre_processor.PreProcessor('test_data/test_url.txt')
        self.assertEqual(ppr.working_txt.count('http'), 3)
        ppr.remove_urls()
        self.assertEqual(ppr.working_txt.count('http'), 0)

    def test_aggregate(self):
        ppr = pre_processor.PreProcessor('test_data/Null POI.md')
        self.assertEqual(ppr.working_txt.count('http'), 13)
        ppr.remove_urls()
        self.assertEqual(ppr.working_txt.count('http'), 0)
        self.assertEqual(ppr.working_txt.count('\n'), 46)
        ppr.remove_newline()
        self.assertEqual(ppr.working_txt.count('\n'), 0)

    def test_process(self):
        ppr = pre_processor.PreProcessor('test_data/Null POI.md')
        ppr.start()
        self.assertTrue(ppr.get_output_file_path())

if __name__ == '__main__':
    unittest.main()
