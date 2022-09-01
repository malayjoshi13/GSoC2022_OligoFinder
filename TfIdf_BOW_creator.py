import csv
import numpy as np
import re 
import enchant
from nltk.stem import PorterStemmer
from regex_extraction import word_processor

dict = enchant.Dict("en_US")
ps = PorterStemmer()


# this part generate tf-idf BOW

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

# Create vocab
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

    non_oligo_sentences = list()
    oligo_sentences = list()
    non_oligo_vocab = list()
    oligo_vocab = list()

    for i in range(len(current_sentence)):
        if is_oligo[i]=="Oligo" and current_sentence[i] not in oligo_sentences: #appends unique sentences only
            processed_sentence = sentence_processor(current_sentence[i])
            # oligo_sentences.append(current_sentence[i])
            oligo_sentences.append(processed_sentence)

            for word in processed_sentence.split():
                if word not in oligo_vocab:
                    processed_word = word_processor(word)
                    if not processed_word: #if not oligo then append that in vocab coz we want that are linked
                        # with oligo in a sentence, but are themselves not an oligo
                        oligo_vocab.append(word)
                        # processed_bow_word = bow_processor(word)
                        # if not processed_bow_word:
                        #     oligo_vocab.append(processed_bow_word) 


        elif is_oligo[i]!="Oligo" and current_sentence[i] not in non_oligo_sentences:
            processed_sentence = sentence_processor(current_sentence[i])
            # oligo_sentences.append(current_sentence[i])
            non_oligo_sentences.append(processed_sentence)

            for word in processed_sentence.split():
                if word not in non_oligo_vocab:
                    processed_word = word_processor(word)
                    if not processed_word: #if not oligo looking sequence then append that in vocab coz 
                        # we want that are linked with oligo in a sentence, but are themselves not an oligo
                        non_oligo_vocab.append(word)

    return non_oligo_sentences, oligo_sentences, non_oligo_vocab, oligo_vocab


# Creating an index for each word in our vocab.
def vocab_elements(vocab):
    index_dict = {} 
    i = 0
    for word in vocab:
        index_dict[word] = i
        i += 1
    return index_dict


# Create a count dictionary to keep the count of the number of documents containing the given word
def count_dict(sentences, vocab):
    word_count = {}
    for word in vocab:
        word_count[word] = 0
        for sent in sentences:
            if word in sent:
                word_count[word] += 1
    return word_count


# Term Frequency
def termfreq(sentence, word):
    N = len(sentence.split())
    occurance = 0
    for token in sentence.split():
        if token == word:
            occurance+=1
    return occurance/N #ocurrennce of a word in a sentence/total length of that sentence
    #multiple sentences==multiple documents


#Inverse Document Frequency
def inverse_doc_freq(word, document_len, word_count):
    try:
        word_occurance = word_count[word] + 1
    except:
        word_occurance = 1 
    return np.log(document_len/word_occurance) #np.log(total number of sentences in oligo passage/occurence of a word in oligo passage)


#Combining the TF-IDF functions
def tf_idf(sentences, vocab, sentence):
    word_count = count_dict(sentences, vocab)
    document_len = len(sentences)

    tf_idf_vec = {}
    for word in sentence.split():
        if word in vocab:
            tf = termfreq(sentence, word)
            idf = inverse_doc_freq(word, document_len, word_count)
            value = tf*idf

            if value>0.01:
                if word not in tf_idf_vec:
                    tf_idf_vec[word] = [value]
                else:
                    tf_idf_vec[word].append(value)

    return tf_idf_vec


def above_threshold_tfidf_words(sentences, vocab):
    tf_idf_vec_final = {}
    for sentence in sentences:
        tf_idf_vec = tf_idf(sentences, vocab, sentence)
        tf_idf_vec_final.update(tf_idf_vec)

    for i in tf_idf_vec_final:
        sum = 0
        # print(str(i)+": "+str(tf_idf_vec_final[i])) #before

        for j in tf_idf_vec_final[i]:
            sum += j
        tf_idf_vec_final[i] = sum/len(tf_idf_vec_final[i]) #if three tfidf are added then divide by 3
        
        # print(str(i)+": "+str(tf_idf_vec_final[i])) #after

    return tf_idf_vec_final





# main code
# filename = "oligos.csv"
# non_oligo_sentences, oligo_sentences, non_oligo_vocab, oligo_vocab = create_vocab(filename)

# above_threshold_tfidf_oligo_words_var = above_threshold_tfidf_words(oligo_sentences, oligo_vocab)
# with open('oligo_words_with_tfidf.txt', 'w') as f3:
#     f3.write(str(above_threshold_tfidf_oligo_words_var))
# ###
# oligo_words = above_threshold_tfidf_oligo_words_var.keys()
# with open('oligo_words.txt', 'w') as f1:
#     f1.write(str(oligo_words))

# above_threshold_tfidf_nonoligo_words_var = above_threshold_tfidf_words(non_oligo_sentences, non_oligo_vocab)
# with open('non_oligo_words_with_tfidf.txt', 'w') as f4:
#     f4.write(str(above_threshold_tfidf_nonoligo_words_var))
# ###
# non_oligo_words = above_threshold_tfidf_nonoligo_words_var.keys()
# with open('non_oligo_words.txt', 'w') as f2:
#     f2.write(str(non_oligo_words))


