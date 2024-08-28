sentences = [
    ['this', 'is', 'the', 'first', 'sentence'],
    ['this', 'is', 'the', 'second', 'sentence'],
    ['and', 'this', 'is', 'another', 'sentence']
]

from gensim.models import Word2Vec

# Train the model
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

# Get the vector for a specific word
vector = model.wv['sentence']
print(vector)

# Get the most similar words
similar_words = model.wv.most_similar('sentence')
print(similar_words)

# Save the model
model.save('./output/word2vec.model')

# Load the model
model = Word2Vec.load('./output/word2vec.model')

from gensim.models import KeyedVectors
model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
vector = model['word']
print(vector)
similar_words = model.most_similar('word')
print(similar_words)

