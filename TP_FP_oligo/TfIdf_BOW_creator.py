import csv
from TP_FP_oligo.sentence_processor import sentence_processor
import numpy as np
from RegexRules.combine_rules import word_processor
from configure import setConfiguration


# this part generate tf-idf BOW

# create vocab
def create_vocab(filename):
    # open the file in read mode
    read_file = open(filename, 'r')
    
    # create dictreader object
    file = csv.DictReader(read_file)
    
    # create empty lists
    current_sentence = list()
    is_oligo = list()
    
    # iterate over each row of CSV and append values corresponding to "Current Sentence"
    # and "TP or FP Oligo (manual)" columns to empty lists
    for col in file:
        current_sentence.append(col['Current Sentence'])
        is_oligo.append(col['TP or FP Oligo (manual)'])

    non_oligo_sentences = list()
    oligo_sentences = list()
    non_oligo_vocab = list()
    oligo_vocab = list()

    for i in range(len(current_sentence)): # pick ith sentence of CSV
        if is_oligo[i]!="" and is_oligo[i]!=None: # pick ith manual-tagging and check if it's not empty (i.e there must be tag of TP or FP)
            # to create BOW, we want sentences to have words that are pre-processed & be present in engish dictionary 
            processed_sentence = sentence_processor(current_sentence[i])
            # if manual-tag is "Oligo" and the corresponding sentence is not already appended (keeps check for unique sentences)
            if is_oligo[i]=="Oligo":
                if processed_sentence not in oligo_sentences: 
                    oligo_sentences.append(processed_sentence)

                    for word in processed_sentence.split():
                        if word not in oligo_vocab:
                            processed_word = word_processor(word)
                            if not processed_word: #if structure of word is not like oligo, then append that in vocab 
                                # because we want words that are linked with oligo in a sentence, but are themselves not an oligo
                                oligo_vocab.append(word)

            elif is_oligo[i]!="Oligo":
                if processed_sentence not in non_oligo_sentences:
                    non_oligo_sentences.append(processed_sentence)

                    for word in processed_sentence.split():
                        if word not in non_oligo_vocab:
                            processed_word = word_processor(word)
                            if not processed_word: 
                                non_oligo_vocab.append(word)

    return non_oligo_sentences, oligo_sentences, non_oligo_vocab, oligo_vocab


# create an index for each word in our vocab.
def vocab_elements(vocab):
    index_dict = {} 
    i = 0
    for word in vocab:
        index_dict[word] = i
        i += 1
    return index_dict


# create a count dictionary to keep the count of the number of documents containing the given word
def count_dict(sentences, vocab):
    word_count = {}
    for word in vocab:
        word_count[word] = 0
        for sent in sentences:
            if word in sent:
                word_count[word] += 1
    return word_count


# term frequency
def termfreq(sentence, word):
    N = len(sentence.split())
    occurance = 0
    for token in sentence.split():
        if token == word:
            occurance+=1
    return occurance/N #ocurrennce of a word in a sentence/total length of that sentence
    #multiple sentences==multiple documents


# inverse document frequency
def inverse_doc_freq(word, document_len, word_count):
    try:
        word_occurance = word_count[word] + 1
    except:
        word_occurance = 1 
    return np.log(document_len/word_occurance) #np.log(total number of sentences in oligo passage/occurence of a word in oligo passage)


# combining the TF-IDF functions
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


# make list of all words with tf_idf score above a certain threshold decided by "tf_idf" function (present above)
def above_threshold_tfidf_words(sentences, vocab):
    tf_idf_vec_final = {}
    for sentence in sentences:
        tf_idf_vec = tf_idf(sentences, vocab, sentence)
        tf_idf_vec_final.update(tf_idf_vec)

    for i in tf_idf_vec_final:
        sum = 0
        for j in tf_idf_vec_final[i]:
            sum += j
        tf_idf_vec_final[i] = sum/len(tf_idf_vec_final[i]) #if three tfidf are added then divide by 3
    return tf_idf_vec_final


# main driver code block that create BOWs corresponding to oligos and non-oligos mentions
def create_BOW():

    _, _, output_CSVname, oligo_BOW_filename, non_oligo_BOW_filename = setConfiguration()

    non_oligo_sentences, oligo_sentences, non_oligo_vocab, oligo_vocab = create_vocab(output_CSVname)


    above_threshold_tfidf_oligo_words_var = above_threshold_tfidf_words(oligo_sentences, oligo_vocab)
    oligo_words = above_threshold_tfidf_oligo_words_var.keys()
    with open(oligo_BOW_filename, 'w') as f1:
        f1.write(str(oligo_words))

    # uncomment if you want to view tf-idf score corresponding to each word
    # with open('oligo_words_with_tfidf.txt', 'w') as f3:
    #     f3.write(str(above_threshold_tfidf_oligo_words_var))


    above_threshold_tfidf_nonoligo_words_var = above_threshold_tfidf_words(non_oligo_sentences, non_oligo_vocab)
    non_oligo_words = above_threshold_tfidf_nonoligo_words_var.keys()
    with open(non_oligo_BOW_filename, 'w') as f2:
        f2.write(str(non_oligo_words))

    # uncomment if you want to view tf-idf score corresponding to each word
    # with open('non_oligo_words_with_tfidf.txt', 'w') as f4:
    #     f4.write(str(above_threshold_tfidf_nonoligo_words_var))
