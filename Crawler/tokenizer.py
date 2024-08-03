#import nltk
#import re
import spacy
import pre_processor

#from nltk.tokenize import word_tokenize

sp = spacy.load('en_core_web_sm')

def process(path):
    ppr = pre_processor.PreProcessor()

    working_txt = open(path, 'r').read()
    print(working_txt)

    print('\n\n\n')

    clean_txt = ppr.remove_urls(working_txt)
    clean_txt = ppr.remove_newline(clean_txt)
    print(clean_txt)

    print('\n\n\n')
    #tokens = word_tokenize(clean_txt)
    tokens = sp(clean_txt)
    for token in tokens:
        print(token.text)
    #print(tokens)

test_file = '/Users/binwei/OneDrive - Microsoft/ObsidianNote/2 Area/MSFT - Search/Null POI.md'

process(test_file)