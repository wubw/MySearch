from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize

txt = None
with open('test_data/Null POI.md', 'r', encoding='utf-8') as file:
    txt = file.read()

lines = txt.splitlines()
print(lines)

# define a list of documents.
data = ["This is the first document",
        "This is the second document",
        "This is the third document",
        "This is the fourth document"]

data = lines

# preproces the documents, and create TaggedDocuments
tagged_data = [TaggedDocument(words=word_tokenize(doc.lower()), tags=[str(i)]) for i, doc in enumerate(data)]

# train the Doc2vec model
model = Doc2Vec(vector_size=50, min_count=2, epochs=50)
model.build_vocab(tagged_data)
model.train(tagged_data, total_examples=model.corpus_count, epochs=model.epochs)
 
# get the document vectors
document_vectors = [model.infer_vector(word_tokenize(doc.lower())) for doc in data]

import numpy as np
np_arr = np.array(document_vectors)
print(np_arr.shape)

#  print the document vectors
for i, doc in enumerate(data):
    print("Document", i+1, ":", doc)
    print("Vector:", document_vectors[i])
    print()

import pynndescent

index = pynndescent.NNDescent(np_arr)

neighbors = index.query([model.infer_vector(word_tokenize("what is poi?".lower()))])
print(neighbors)