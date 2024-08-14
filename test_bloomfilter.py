import bloomfilter
import unittest

class TestBloomFilter(unittest.TestCase):
    def test_basic_example(self):
        bloom = bloomfilter.BloomFilter(size=500, hash_count=7)
        bloom.add("example")
        bloom.add("hello")
        bloom.add("world")
        bloom.add("microsoft")
        
        self.assertTrue(bloom.check("example"))
        self.assertFalse(bloom.check("test"))

if __name__ == '__main__':
    unittest.main()
