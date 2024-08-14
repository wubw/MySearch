import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

#import spacy
#sp = spacy.load('en_core_web_sm')
#print('\n\n\n')
#tokens = sp(clean_txt)
#print(tokens)
#for token in tokens:
#    print(token.text)

class Tokenizer:
    def __init__(self, text) -> None:
        self.working_txt = text
        nltk.download('punkt')
        nltk.download('stopwords')

    def start(self):
        tokens = word_tokenize(self.working_txt) 

        stemmer = PorterStemmer() 
        stemmed_tokens = [stemmer.stem(token) for token in tokens]
        #print(stemmed_tokens)

        
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [token for token in stemmed_tokens if token.lower() not in stop_words]
        #print(filtered_tokens)

        return filtered_tokens
