from abc import ABC, abstractmethod
import glob
import pre_processor
import tokenizer
import search_item

class IndexBase(ABC):
    @abstractmethod
    def ingest(self, file_path):
        pass

    def ingest_batch(self, filter):
        files = []
        for f in glob.glob(filter):
            files.append(f)

        #print(files)
        for f in files:
            print(f)
            self.ingest(f)

    def get_tokens(self, fi):
        ppr = pre_processor.PreProcessor(fi)
        ppr.start()

        t = tokenizer.Tokenizer(fi)
        tokens = t.start()

        return tokens
    
    def get_tokens_searchtxt(self, search_txt):
        si = search_item.SearchItem(search_txt, None)
        ppr = pre_processor.PreProcessor(si)
        ppr.start()

        t = tokenizer.Tokenizer(si)
        tokens = t.start()

        return tokens
    
    def ranking(self, results_by_path):
        #print(results_by_path)
        sorted_keys = sorted(results_by_path, key=results_by_path.get, reverse=True)

        return sorted_keys
