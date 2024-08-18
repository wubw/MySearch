import unittest
import file_item
import pre_processor

class TestPreProcessor(unittest.TestCase):

    def test_remove_newlines(self):
        fi = file_item.FileItem('test_data/test_url.txt')
        ppr = pre_processor.PreProcessor(fi)
        self.assertEqual(ppr.working_txt.count('\n'), 9)
        ppr.remove_newline()
        self.assertEqual(ppr.working_txt.count('\n'), 0)

    def test_remove_url(self):
        fi = file_item.FileItem('test_data/test_url.txt')
        ppr = pre_processor.PreProcessor(fi)
        self.assertEqual(ppr.working_txt.count('http'), 3)
        ppr.remove_urls()
        self.assertEqual(ppr.working_txt.count('http'), 0)

    def test_aggregate(self):
        fi = file_item.FileItem('test_data/Null POI.md')
        ppr = pre_processor.PreProcessor(fi)
        self.assertEqual(ppr.working_txt.count('http'), 13)
        ppr.remove_urls()
        self.assertEqual(ppr.working_txt.count('http'), 0)
        self.assertEqual(ppr.working_txt.count('\n'), 46)
        ppr.remove_newline()
        self.assertEqual(ppr.working_txt.count('\n'), 0)

    def test_process(self):
        fi = file_item.FileItem('test_data/Null POI.md')
        ppr = pre_processor.PreProcessor(fi)
        ppr.start()
        self.assertIsNotNone(ppr.si.ppr_txt)

if __name__ == '__main__':
    unittest.main()
