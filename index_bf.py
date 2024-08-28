# index supported by bloom filter

import file_item
import bloomfilter
import index_base

class IndexBloomFilter(index_base.IndexBase):
    
    def __init__(self) -> None:
        self.file_items = []

    def ingest(self, file_path):
        fi = file_item.FileItem(file_path)
        bf = bloomfilter.BloomFilter(size=5000, hash_count=7)
        fi.bf = bf
        if fi not in self.file_items:
            self.file_items.append(fi)
        self.process_file_item(fi)

    def process_file_item(self, fi):
        tokens = super().get_tokens(fi)

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
        tokens = self.get_tokens_searchtxt(search_txt)

        token_check_count = {}
        for t in tokens:
            token_check_count[t] = self.check_token(t)
        
        results_by_path = {}
        for k in token_check_count:
            #print(k + ": ")
            for fi in token_check_count[k]:
                #print(fi.path)
                if fi.path not in results_by_path:
                    results_by_path[fi.path] = 1
                else:
                    results_by_path[fi.path] = results_by_path[fi.path] + 1

        ret = super().ranking(results_by_path)
        print(ret)

        return ret
