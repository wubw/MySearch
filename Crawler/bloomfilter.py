# Step 1: Install bitarray
# pip install bitarray

# Step 2: Import the necessary modules
from bitarray import bitarray
import mmh3

# Step 3: Define the Bloom filter class
class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    # Step 4: Implement the add method
    def add(self, item):
        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size
            self.bit_array[index] = 1

    # Step 5: Implement the check method
    def check(self, item):
        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size
            if self.bit_array[index] == 0:
                return False
        return True

# Example usage
bloom = BloomFilter(size=500, hash_count=7)
bloom.add("example")
print(bloom.check("example"))  # Output: True
print(bloom.check("test"))     # Output: False
