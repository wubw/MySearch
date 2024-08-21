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

        ret = self.ranking(results_by_path)
        print(ret)

        return ret

    def ranking(self, results_by_path):
        print(results_by_path)
        sorted_keys = sorted(results_by_path, key=results_by_path.get, reverse=True)

        return sorted_keys
