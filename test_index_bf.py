import unittest
import index_bf

class TestIndexBloomFilter(unittest.TestCase):

    def test_ingest(self):
        idx_bf = index_bf.IndexBloomFilter()
        self.assertEqual(len(idx_bf.file_items), 0)
        idx_bf.ingest('test_data/Null POI.md')

        self.assertEqual(len(idx_bf.file_items), 1)
        self.assertFalse(idx_bf.file_items[0].bf.check("example"))
        self.assertTrue(idx_bf.file_items[0].bf.check("poi"))
        self.assertTrue(idx_bf.file_items[0].bf.check("recrawl"))
        self.assertTrue(idx_bf.file_items[0].bf.check("loop"))

    def test_check_token(self):
        idx_bf = index_bf.IndexBloomFilter()
        idx_bf.ingest('test_data/Null POI.md')

        ret = idx_bf.check_token("poi")
        self.assertEqual(len(ret), 1)

        ret = idx_bf.check_token("world")
        self.assertEqual(len(ret), 0)

    def test_check_toeken_batch(self):
        idx_bf = index_bf.IndexBloomFilter()
        idx_bf.ingest_batch('test_data/*.md')

        ret = idx_bf.check_token("poi")
        self.assertGreater(len(ret), 2)

        ret = idx_bf.check_token("world")
        self.assertEqual(len(ret), 0)

    def test_search(self):
        idx_bf = index_bf.IndexBloomFilter()
        idx_bf.search("hello, world")