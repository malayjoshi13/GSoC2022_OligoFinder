import csv
import numpy as np

#Create vocab
def create_vocab(filename):
    # open the file in read mode
    read_file = open(filename, 'r')
    
    # creating dictreader object
    file = csv.DictReader(read_file)
    
    # creating empty lists
    current_sentence = list()
    is_oligo = list()
    
    # iterating over each row and append
    # values to empty list
    for col in file:
        current_sentence.append(col['Current Sentence'])
        is_oligo.append(col['Is this an oligo?'])
    
    # print('current_sentence:', current_sentence)
    # print('is_oligo:', is_oligo)

    non_oligo_sentences = list()
    oligo_sentences = list()
    non_oligo_sentences_words = list()
    oligo_sentences_words = list()

    for i in range(len(current_sentence)):
        if is_oligo[i]!="Oligo":
            non_oligo_sentences.append(current_sentence[i])
            for word in current_sentence[i].split():
                if word not in non_oligo_sentences_words:
                    non_oligo_sentences_words.append(word)            

        else:
            oligo_sentences.append(current_sentence[i])
            for word in current_sentence[i].split():
                if word not in oligo_sentences_words:
                    oligo_sentences_words.append(word)

    # print(non_oligo_sentences)
    # print(oligo_sentences)
    return non_oligo_sentences, oligo_sentences, non_oligo_sentences_words, oligo_sentences_words

#Creating an index for each word in our vocab.
def vocab_elements(vocab):
    index_dict = {} #Dictionary to store index for each word
    i = 0
    for word in vocab:
        index_dict[word] = i
        i += 1
    return index_dict

#Create a count dictionary to keep the count of the number of documents containing the given word
def count_dict(sentences, vocab):
    word_count = {}
    for word in vocab:
        word_count[word] = 0
        for sent in sentences:
            if word in sent:
                word_count[word] += 1
    return word_count

#Term Frequency
def termfreq(sentences, word):
    N = len(sentences)
    occurance = len([token for token in sentences if token == word])
    return occurance/N #ocurrennce of a word in a sentence/total length of that sentence
    #passage/document has multiple sentences

#Inverse Document Frequency
def inverse_doc_freq(word, document_len, word_count):
    try:
        word_occurance = word_count[word] + 1
    except:
        word_occurance = 1 
    return np.log(document_len/word_occurance) #np.log(total number of sentences in oligo passage/occurence of a word in oligo passage)

#Combining the TF-IDF functions
def tf_idf(sentence, vocab, document_len, word_count):
    index_dict = vocab_elements(vocab)
    tf_idf_vec = np.zeros((len(vocab),))
    for word in sentence.split():
        tf = termfreq(sentence, word)
        idf = inverse_doc_freq(word, document_len, word_count)
        
        value = tf*idf
        tf_idf_vec[index_dict[word]] = value 
    return tf_idf_vec


# main code
filename = "oligos.csv"
non_oligo_sentences, oligo_sentences, non_oligo_sentences_words, oligo_sentences_words = create_vocab(filename)
total_oligo_sentences_len = len(oligo_sentences)
total_non_oligo_sentences_len = len(non_oligo_sentences)

word_count_oligo = count_dict(oligo_sentences, oligo_sentences_words)
word_count_non_oligo = count_dict(non_oligo_sentences, non_oligo_sentences_words)

for oligo_sentence in oligo_sentences:
    tf_idf_vec_oligo = tf_idf(oligo_sentence, oligo_sentences_words, total_oligo_sentences_len, word_count_oligo)

for non_oligo_sentence in non_oligo_sentences:
    tf_idf_vec_non_oligo = tf_idf(non_oligo_sentence, non_oligo_sentences_words, total_non_oligo_sentences_len, word_count_non_oligo)

print(tf_idf_vec_oligo)
print(tf_idf_vec_non_oligo)