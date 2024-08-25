import unittest
import posting_list

class TestPostingList(unittest.TestCase):

    def test_ingest(self):
        pl = posting_list.PostingList()
        self.assertEqual(len(pl.posting_list), 0)

        pl.ingest("doc_1", ["hello"])
        self.assertEqual(len(pl.posting_list), 1)

    def test_batch_ingest(self):
        docs = {
            "doc1": ["the", "cat", "sat", "on", "the", "mat"],
            "doc2": ["the", "dog", "sat", "on", "the", "log"],
            "doc3": ["the", "cat", "lay", "on", "the", "mat"],
            "doc4": ["the", "dog", "lay", "on", "the", "log"]
        }
        pl = posting_list.PostingList()
        self.assertEqual(len(pl.posting_list), 0)

        pl.batch_ingest(docs)
        self.assertEqual(len(pl.posting_list), 8)
