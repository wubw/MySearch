class PostingList:
    def __init__(self):
        self.posting_list = {}
    
    def batch_ingest(self, docs):
        for doc_id, words in docs.items():
            self.ingest(doc_id, words)
        return self.posting_list
    
    def ingest(self, doc_id, words):
        for word in words:
            if word not in self.posting_list:
                self.posting_list[word] = [doc_id]
            else:
                self.posting_list[word].append(doc_id)

    def print(self):
        for term, postings in self.posting_list.items():
            print(f"Term: {term}, Postings: {postings}")
