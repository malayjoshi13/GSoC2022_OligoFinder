import re
import enchant
from nltk.stem import PorterStemmer

dict = enchant.Dict("en_US")
ps = PorterStemmer()


def sentence_processor(sentence):
    processed_sentence  = ""
    list_string = sentence.split(' ')
    for word in list_string:
        word = word.lower()
        word = re.sub(r'[^a-z\s]','',word)
        word = ps.stem(word)
        if len(word)>2 and dict.check(word):
            processed_word = word
        else:
            processed_word = ""

        processed_sentence+=" "+processed_word
    return processed_sentence
