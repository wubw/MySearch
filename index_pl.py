import posting_list
import file_item
import pre_processor
import tokenizer
import glob
import search_item

class IndexPostingList:
    
    def __init__(self) -> None:
        self.pl = posting_list.PostingList()

    def ingest(self, file_path):
        fi = file_item.FileItem(file_path)
        fi.tokens = []
        self.process_file_item(fi)
        self.pl.ingest(fi.path, fi.tokens)

    def process_file_item(self, fi):
        ppr = pre_processor.PreProcessor(fi)
        ppr.start()

        t = tokenizer.Tokenizer(fi)
        tokens = t.start()

        for t in tokens:
            fi.tokens.append(t)

    def ingest_batch(self, filter):
        files = []
        for f in glob.glob(filter):
            files.append(f)

        #print(files)
        for f in files:
            print(f)
            self.ingest(f)

    def search (self, search_txt):
        si = search_item.SearchItem(search_txt, None)
        ppr = pre_processor.PreProcessor(si)
        ppr.start()

        t = tokenizer.Tokenizer(si)
        tokens = t.start()

        token_check_count = {}
        for t in tokens:
            if t in self.pl.posting_list:
                token_check_count[t] = self.pl.posting_list[t]

        #print(token_check_count)

        results_by_path = {}
        for k in token_check_count:
            #print(k + ": ")
            for path in token_check_count[k]:
                #print(fi.path)
                if path not in results_by_path:
                    results_by_path[path] = 1
                else:
                    results_by_path[path] = results_by_path[path] + 1
        ret = self.ranking(results_by_path)
        #print(ret)

        return ret

    def ranking(self, results_by_path):
        #print(results_by_path)
        sorted_keys = sorted(results_by_path, key=results_by_path.get, reverse=True)

        return sorted_keys
