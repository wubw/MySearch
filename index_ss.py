from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
import glob
import file_item
import numpy as np
import pynndescent

class IndexSemanticSearch:
    def __init__(self) -> None:
        self.file_items = []

    def ingest(self, file_path):
        fi = file_item.FileItem(file_path)
        fi.lines = []
        for l in fi.txt.splitlines():
            if l.strip() != '':
                fi.lines.append(l)
        print(fi.lines)
        self.file_items.append(fi)

    def ingest_batch(self, filter):
        files = []
        for f in glob.glob(filter):
            files.append(f)

        #print(files)
        for f in files:
            print(f)
            self.ingest(f)

    def build(self):
        data = self.file_items[0]
        tagged_data = [TaggedDocument(words=word_tokenize(doc.lower()), tags=[str(i)]) for i, doc in enumerate(data.lines)]
        self.model = Doc2Vec(vector_size=50, min_count=2, epochs=50)
        self.model.build_vocab(tagged_data)
        self.model.train(tagged_data, total_examples=self.model.corpus_count, epochs=self.model.epochs)
        self.document_vectors = [self.model.infer_vector(word_tokenize(doc.lower())) for doc in data.lines]

    def display_index(self):
        data = self.file_items[0]
        np_arr = np.array(self.document_vectors)
        print(np_arr.shape)

        #  print the document vectors
        for i, doc in enumerate(data.lines):
            print("Document", i+1, ":", doc)
            print("Vector:", self.document_vectors[i])
            print()

    def search(self, search_txt):
        np_arr = np.array(self.document_vectors)
        index = pynndescent.NNDescent(np_arr)

        neighbors = index.query([self.model.infer_vector(word_tokenize(search_txt.lower()))], epsilon=0.0)
        print(neighbors)

idxss = IndexSemanticSearch()
idxss.ingest('test_data/Null POI.md')
idxss.build()
idxss.display_index()
idxss.search("poi")
