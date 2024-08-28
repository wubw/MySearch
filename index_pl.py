import posting_list
import file_item
import index_base

class IndexPostingList(index_base.IndexBase):
    
    def __init__(self) -> None:
        self.pl = posting_list.PostingList()

    def ingest(self, file_path):
        fi = file_item.FileItem(file_path)
        fi.tokens = []
        self.process_file_item(fi)
        self.pl.ingest(fi.path, fi.tokens)

    def process_file_item(self, fi):
        tokens = super().get_tokens(fi)

        for t in tokens:
            fi.tokens.append(t)

    def search (self, search_txt):
        tokens = self.get_tokens_searchtxt(search_txt)

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
        ret = super().ranking(results_by_path)
        #print(ret)

        return ret
