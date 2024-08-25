import unittest
import index_pl

class TestIndexPostingList(unittest.TestCase):

    def test_ingest(self):
        ipl = index_pl.IndexPostingList()
        self.assertEqual(len(ipl.pl.posting_list), 0)

        ipl.ingest('test_data/Null POI.md')
        self.assertGreater(len(ipl.pl.posting_list), 130)

    def test_batch_ingest(self):
        ipl = index_pl.IndexPostingList()
        self.assertEqual(len(ipl.pl.posting_list), 0)

        ipl.ingest_batch('test_data/*.md')
        self.assertGreater(len(ipl.pl.posting_list), 800)

    def test_batch_search(self):
        ipl = index_pl.IndexPostingList()
        self.assertEqual(len(ipl.pl.posting_list), 0)

        ipl.ingest_batch('test_data/*.md')
        self.assertGreater(len(ipl.pl.posting_list), 800)

        ret = ipl.search('hello')
        self.assertEqual(len(ret), 0)
        ret = ipl.search('cut')
        self.assertGreaterEqual(len(ret), 1)
        ret = ipl.search('poi')
        self.assertGreaterEqual(len(ret), 3)
        self.assertEqual(ret[0], 'test_data\\Null POI.md')
