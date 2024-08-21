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
        idx_bf.ingest_batch('test_data/*.md')
        ret = idx_bf.search("hello, world")
        self.assertEqual(len(ret), 0)

        ret = idx_bf.search("test poi loop please")
        self.assertGreaterEqual(len(ret), 4)
        self.assertEqual(ret[0], 'test_data\\Null POI.md')

    def test_ranking(self):
        input_data = {'a': 1, 'b': 2, 'c': 3, 'd': 5, 'e': 4}
        idx_bf = index_bf.IndexBloomFilter()
        ret = idx_bf.ranking(input_data)
        self.assertGreaterEqual(len(ret), 5)
        self.assertEqual(ret[0], 'd')
        self.assertEqual(ret[1], 'e')
        self.assertEqual(ret[2], 'c')
        self.assertEqual(ret[3], 'b')
        self.assertEqual(ret[4], 'a')
