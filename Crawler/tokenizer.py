#import spacy
import pre_processor

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

#sp = spacy.load('en_core_web_sm')

def process(path):
    ppr = pre_processor.PreProcessor(path)

    print(ppr.working_txt)

    print('\n\n\n')

    ppr.process()
    print(ppr.working_txt)

    #print('\n\n\n')
    #tokens = sp(clean_txt)
    #print(tokens)
    #for token in tokens:
    #    print(token.text)

    print('\n\n\n')
    nltk.download('punkt')
    tokens = word_tokenize(ppr.working_txt) 

    stemmer = PorterStemmer() 
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    #print(stemmed_tokens)

    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in stemmed_tokens if token.lower() not in stop_words]
    print(filtered_tokens)

    return filtered_tokens


test_file = 'C:/Users/binweiwu.REDMOND/OneDrive - Microsoft/ObsidianNote/2 Area/MSFT - Search/Null POI.md'

process(test_file)