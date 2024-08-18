# index supported by bloom filter

import file_item
import search_item
import pre_processor
import tokenizer
import bloomfilter
import glob

class IndexBloomFilter:
    
    def __init__(self) -> None:
        self.file_items = []

    def ingest(self, file_path):
        fi = file_item.FileItem(file_path)
        bf = bloomfilter.BloomFilter(size=5000, hash_count=7)
        fi.bf = bf
        if fi not in self.file_items:
            self.file_items.append(fi)
        self.process_file_item(fi)

    def ingest_batch(self, filter):
        files = []
        for f in glob.glob(filter):
            files.append(f)

        #print(files)
        for f in files:
            print(f)
            self.ingest(f)

    def process_file_item(self, fi):
        ppr = pre_processor.PreProcessor(fi)
        ppr.start()

        t = tokenizer.Tokenizer(fi)
        tokens = t.start()

        for t in tokens:
            fi.bf.add(t)

    def check_token(self, token):
        ret = []
        for fi in self.file_items:
            if fi.bf.check(token):
                #print('check token: ' + fi.path)
                ret.append(fi)

        return ret

    def search (self, search_txt):
        si = search_item.SearchItem(search_txt, None)
        ppr = pre_processor.PreProcessor(si)
        ppr.start()

        t = tokenizer.Tokenizer(si)
        tokens = t.start()

        print(tokens)
