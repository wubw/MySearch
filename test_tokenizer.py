import pre_processor
import tokenizer
import file_item
import unittest

class TestTokenizer(unittest.TestCase):
    def test_start(self):
        fi = file_item.FileItem('test_data/Null POI.md')
        ppr = pre_processor.PreProcessor(fi)
        ppr.start()

        t = tokenizer.Tokenizer(fi)
        tokens = t.start()
        self.assertGreater(len(tokens), 20)

if __name__ == '__main__':
    unittest.main()
