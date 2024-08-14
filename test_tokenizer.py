import pre_processor
import tokenizer
import unittest

class TestTokenizer(unittest.TestCase):
    def test_start(self):
        ppr = pre_processor.PreProcessor('test_data/Null POI.md')
        ppr.start()

        t = tokenizer.Tokenizer(ppr.working_txt)
        tokens = t.start()
        self.assertGreater(len(tokens), 20)

if __name__ == '__main__':
    unittest.main()
